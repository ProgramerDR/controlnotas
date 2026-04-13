from flask import Flask,render_template,request,redirect,session
from database import conectar
from database import obtenerusuarios
from database import insertar_estudiante, estudiante_existe
from dashprincipal import creartablero
import pandas as pd
import unicodedata
import mysql.connector


app = Flask(__name__)

# CLAVE NECESARIA PARA USAR SESSION

app.secret_key = "40414732"

# crear dashboard
# creartablero(app)

#evitar cache  en paginas protegidas
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache ,must-revalidate , max-age=0"
    response.headers["Pragma"]= "no-cache"
    response.headers["Expires"] = "0"

    return response

@app.route("/",methods=["GET","POST"])
def login():

    #verificar si el formulario fue enviado
    if request.method == "POST":
        #capturar los datos del formulario

        username = request.form["username"]
        password = request.form["password"]

        usuario = obtenerusuarios(username)

        #verificar si existe
        if usuario:

          if usuario["password"] == password:

              #creo la sesion del usuario
              session["username"] = usuario["username"]
              session["rol"] = usuario["rol"]

              return redirect("/dashprincipal")
          else:
              return "Contraseña incorrecta"
        else:
             return "Usuario no existe"

    return  render_template("login.html")
@app.route("/dashprincipal")
def dashprinci():
    if "username"  not in session:
        return redirect("/")

    return render_template("dashprinci.html", usuario=session["username"])

@app.route("/logout")
def logout():
   session.clear()
   return redirect("/")


@app.route("/registro_estudiante", methods=["GET","POST"])
def registroestudiante():
    if "username" not in session:
        return ("/")

    if request.method == "POST":

        nombre = request.form["txtnombre"]
        edad = request.form["txtedad"]
        carrera = request.form["txtcarrera"]
        notauno = float(request.form["txtnota1"])
        notados = float(request.form["txtnota2"])
        notatres = float(request.form["txtnota3"])
        #calcular el promedio
        promedio = round((notauno+notados+notatres)/ 3,2)


        #calcular el desempeño
        desempeno = calculardesempeño(promedio)

        #llamar la conexion
       # conn = conectar()
        #cursor =conn.cursor()
        
        #pequeña verificacion
        if estudiante_existe(nombre, carrera):
            return "El estudiante ya esta hace rato"
        
        #si no existe lo mete        

        insertar_estudiante(nombre,edad,carrera,notauno,notados,notatres,promedio,desempeno)

        return redirect("/dashprincipal")
    
    return  render_template("registro_estudiante.html")

#funcion para quitar acentos
def quitar(texto):
    if pd.isna(texto):
        return texto


    texto = str(texto)

    return ''.join(
            c for  c in unicodedata.normalize('NFD',texto)
            if unicodedata.category(c) != 'Mn'
        )

#clasificar el desempeño
def calculardesempeño(prom):
    if prom >=4.5:
            return "Excelente"
    elif prom >=4:
            return "Bueno"
    elif prom >=3:
            return "Regular"
    else:
            return "Bajo"


@app.route("/cargamasiva", methods=["GET","POST"])
def carga_masiva():


    if request.method == "POST":

        archivo = request.files["txtarchivo"]

        # leer archivo
        df = pd.read_excel(archivo)
        
        #contadorsitos
        
        insertados = 0
        rechazados_count = 0
        duplicados = 0
        rechazados = []

        # limpiar datos
        df["Nombre"] = df["Nombre"].astype(str).str.strip()
        df["Carrera"] = df["Carrera"].astype(str).str.strip()

        conn = conectar()
        cursor = conn.cursor()

        query_insert = """INSERT INTO estudiantes
        (Nombre,Edad,Carrera,nota1,nota2,nota3,Promedio,Desempeño)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

        for _, row in df.iterrows():

            nombre = row["Nombre"]
            edad = row["Edad"]
            carrera = row["Carrera"]
            nota1 = row["Nota1"]
            nota2 = row["Nota2"]
            nota3 = row["Nota3"]

            motivo = ""
            insertados += 1
            # validar datos faltantes
            if pd.isna(nombre) or pd.isna(edad) or pd.isna(carrera) or pd.isna(nota1) or pd.isna(nota2) or pd.isna(nota3):
                motivo = "Datos faltantes"

            # validar edad negativa
            elif edad < 0:
                motivo = "Edad negativa"

            # validar notas
            elif (nota1 < 0 or nota1 > 5 or
                  nota2 < 0 or nota2 > 5 or
                  nota3 < 0 or nota3 > 5):
                motivo = "Notas inválidas"

            # validar duplicados
            else:
                cursor.execute(
                    "SELECT * FROM estudiantes WHERE Nombre=%s AND Carrera=%s",
                    (nombre, carrera)
                )

                if cursor.fetchone():
                    motivo = "Estudiante duplicado"
                    duplicados += 1

            # si hay error  guardar en rechazados
            if motivo != "":
                rechazados.append({
                    "Nombre": nombre,
                    "Edad": edad,
                    "Carrera": carrera,
                    "Nota1": nota1,
                    "Nota2": nota2,
                    "Nota3": nota3,
                    "Motivo": motivo
                })
                rechazados_count += 1

            else:
                promedio = round((nota1 + nota2 + nota3) / 3, 2)
                desempeno = calculardesempeño(promedio)

                cursor.execute(query_insert, (
                    nombre,
                    edad,
                    carrera,
                    nota1,
                    nota2,
                    nota3,
                    promedio,
                    desempeno
                ))

        conn.commit()
        conn.close()

        # generar archivo de rechazados
        if len(rechazados) > 0:
            df_rechazados = pd.DataFrame(rechazados)
            df_rechazados.to_excel("rechazados.xlsx", index=False)

        return render_template(
            "estadisticas_cargue.html",
            insertados=insertados,
            rechazados=rechazados_count,
            duplicados=duplicados
        )

    return render_template("carga_masiva.html")

@app.route("/ranking")
def ranking():

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT Nombre, Carrera, Promedio
    FROM estudiantes
    ORDER BY Promedio DESC
    LIMIT 10
    """

    cursor.execute(query)

    ranking = cursor.fetchall()

    conn.close()

    return render_template("ranking.html", ranking=ranking)
    


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))