import pandas as pd
import plotly.express as px
import dash
from dash import html, Input, Output, dcc
from dash import dash_table
from database import obtenerestudiantes


def creartablero(server):

    dataf = obtenerestudiantes()

    appnotas = dash.Dash(
        __name__,
        server=server,
        url_base_pathname="/dashprincipal/",
        suppress_callback_exceptions=True
    )

    appnotas.layout = html.Div([

        html.H1(
            "TABLERO AVANZADO",
            style={
                "textAlign": "center",
                "backgroundColor": "#1E1BD2",
                "color": "white",
                "padding": "20px"
            }
        ),

        # FILTROS
        html.Div([

            html.Label("Seleccionar carrera"),

            dcc.Dropdown(
                id="filtro_carrera",
                options=[{"label": c, "value": c} for c in sorted(dataf["Carrera"].unique())],
                value=None,
                placeholder="Todas las carreras"
            ),

            html.Br(),

            html.Label("Rango de edad"),

            dcc.RangeSlider(
                id="slider_edad",
                min=dataf["Edad"].min(),
                max=dataf["Edad"].max(),
                step=1,
                value=[dataf["Edad"].min(), dataf["Edad"].max()],
                tooltip={"placement": "bottom", "always_visible": True}
            ),

            html.Br(),

            html.Label("Rango promedio"),

            dcc.RangeSlider(
                id="slider_promedio",
                min=0,
                max=5,
                step=0.5,
                value=[0, 5],
                tooltip={"placement": "bottom", "always_visible": True}
            )

        ], style={"width": "80%", "margin": "auto"}),

        html.Br(),

        # KPIs
        html.Div(
            id="kpis",
            style={"display": "flex", "justifyContent": "space-around"}
        ),

        html.Br(),

        # TABLA PRINCIPAL
        dcc.Loading(
            dash_table.DataTable(
                id="tabla",
                page_size=8,
                filter_action="native",
                sort_action="native",
                row_selectable="multi",
                selected_rows=[],
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "center"}
            ),
            type="circle"
        ),

        html.Br(),

        dcc.Input(
            id="busqueda",
            type="text",
            placeholder="Buscar estudiante"
        ),

        html.Br(),

        # AUTO REFRESH
        dcc.Interval(
            id="intervalo",
            interval=10000,
            n_intervals=0
        ),

        html.Br(),

        # ALERTA
        html.H3(
            "estudiantes mas afuera que adentro",
            style={"textAlign": "center", "color": "red"}
        ),

        dash_table.DataTable(
            id="tabla_riesgo",
            style_table={"width": "50%", "margin": "auto"},
            style_cell={"textAlign": "center"},
            page_size=5
        ),

        html.Br(),

        # RANKING
        html.H3(
            "Ranking de mejores estudiantes",
            style={"textAlign": "center", "color": "green"}
        ),

        dash_table.DataTable(
            id="tabla_ranking",
            style_table={"width": "60%", "margin": "auto"},
            style_cell={"textAlign": "center"},
            page_size=10
        ),

        html.Br(),

        # GRAFICO DETALLADO
        dcc.Loading(
            dcc.Graph(id="gra_detallado"),
            type="default"
        ),

        html.Br(),

        # GRAFICOS
        dcc.Tabs([

            dcc.Tab(label="Histograma", children=[dcc.Graph(id="histograma")]),

            dcc.Tab(label="Dispersion", children=[dcc.Graph(id="dispersion")]),

            dcc.Tab(label="Desempeño", children=[dcc.Graph(id="pie")]),

            dcc.Tab(label="Promedio por Carrera", children=[dcc.Graph(id="barras")])

        ])
    ])

    # CALLBACK PRINCIPAL
    @appnotas.callback(
        Output("tabla", "data"),
        Output("tabla", "columns"),
        Output("kpis", "children"),
        Output("histograma", "figure"),
        Output("dispersion", "figure"),
        Output("pie", "figure"),
        Output("barras", "figure"),
        Output("tabla_riesgo", "data"),
        Output("tabla_riesgo", "columns"),
        Output("tabla_ranking", "data"),
        Output("tabla_ranking", "columns"),

        Input("filtro_carrera", "value"),
        Input("slider_edad", "value"),
        Input("slider_promedio", "value"),
        Input("busqueda", "value"),
        Input("intervalo", "n_intervals")
    )

    def actualizar_comp(carrera, rangoedad, rangoprome, busqueda, n_intervals):

        dataf = obtenerestudiantes()

        # FILTRO
        filtro = dataf[
            (dataf["Edad"] >= rangoedad[0]) &
            (dataf["Edad"] <= rangoedad[1]) &
            (dataf["Promedio"] >= rangoprome[0]) &
            (dataf["Promedio"] <= rangoprome[1])
        ]

        if carrera:
            filtro = filtro[filtro["Carrera"] == carrera]

        if busqueda:
            filtro = filtro[
                filtro.apply(lambda row: busqueda.lower() in str(row).lower(), axis=1)
            ]

        # KPIs
        promedio = round(filtro["Promedio"].mean(), 2) if len(filtro) > 0 else 0
        total = len(filtro)
        maximo = round(filtro["Promedio"].max(), 2) if len(filtro) > 0 else 0

        kpis = [
            html.Div([html.H4("Promedio"), html.H2(promedio)],
                     style={"backgroundColor": "#3498db", "color": "white", "padding": "15px", "borderRadius": "10px"}),

            html.Div([html.H4("Total estudiantes"), html.H2(total)],
                     style={"backgroundColor": "#2ecc71", "color": "white", "padding": "15px", "borderRadius": "10px"}),

            html.Div([html.H4("Máximo"), html.H2(maximo)],
                     style={"backgroundColor": "#9b59b6", "color": "white", "padding": "15px", "borderRadius": "10px"})
        ]

        # GRAFICOS
        histo = px.histogram(filtro, x="Promedio", nbins=10)
        dispersion = px.scatter(filtro, x="Edad", y="Promedio", color="Desempeño", trendline="ols")
        pie = px.pie(filtro, names="Desempeño")

        promedios = dataf.groupby("Carrera")["Promedio"].mean().reset_index()
        barras = px.bar(promedios, x="Carrera", y="Promedio", color="Carrera")

        # RIESGO
        riesgo = dataf[dataf["Promedio"] < 3][["Nombre", "Carrera", "Promedio"]]

        # RANKING
        ranking = dataf.sort_values(by="Promedio", ascending=False).head(10)
        ranking = ranking[["Nombre", "Carrera", "Promedio"]]

        return (
            filtro.to_dict("records"),
            [{"name": i, "id": i} for i in filtro.columns],
            kpis,
            histo,
            dispersion,
            pie,
            barras,
            riesgo.to_dict("records"),
            [{"name": i, "id": i} for i in riesgo.columns],
            ranking.to_dict("records"),
            [{"name": i, "id": i} for i in ranking.columns]
        )

    # GRAFICO DETALLADO
    @appnotas.callback(
        Output("gra_detallado", "figure"),
        Input("tabla", "derived_virtual_data"),
        Input("tabla", "derived_virtual_selected_rows")
    )

    def actualizartab(rows, selected_rows):

        if rows is None:
            return px.scatter(title="Sin datos")

        dff = pd.DataFrame(rows)

        if selected_rows:
            dff = dff.iloc[selected_rows]

        return px.scatter(dff, x="Edad", y="Promedio", color="Desempeño", size="Promedio")

    return appnotas