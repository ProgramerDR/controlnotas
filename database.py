import mysql.connector
import os
import pandas as pd

def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE")
    )

# obtener usuarios
def obtenerusuarios(username):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username=%s", (username,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

# obtener estudiantes
def obtenerestudiantes():
    conn = conectar()
    query = "SELECT * FROM estudiantes"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# verificar si existe estudiante
def estudiante_existe(nombre, carrera):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM estudiantes WHERE Nombre=%s AND Carrera=%s"
    cursor.execute(query, (nombre, carrera))
    
    resultado = cursor.fetchone()
    
    conn.close()
    
    return resultado

# insertar estudiante
def insertar_estudiante(nombre, edad, carrera, nota1, nota2, nota3, promedio, desempeno):
    conn = conectar()
    cursor = conn.cursor()

    query = """INSERT INTO estudiantes 
    (Nombre,Edad,Carrera,nota1,nota2,nota3,Promedio,Desempeno)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

    cursor.execute(query, (nombre, edad, carrera, nota1, nota2, nota3, promedio, desempeno))
    
    conn.commit()
    conn.close()