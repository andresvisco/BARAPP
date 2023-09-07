import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
# Crear la conexión a la base de datos
conn = sqlite3.connect('db/bar.db')
c = conn.cursor()

# Crear la tabla si no existe
c.execute('''
    CREATE TABLE IF NOT EXISTS INGRESOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion varchar(64) NOT NULL,
        importe int(11) NOT NULL,
        fecha datetime NOT NULL,
        tipo varchar(64) NOT NULL,
        socio varchar(64) NOT NULL
    )
''')
conn.commit()

# Función para agregar un nuevo ingreso
def agregar_ingreso(descripcion, importe, fecha, tipo, socio):
    c.execute("INSERT INTO INGRESOS (descripcion, importe, fecha, tipo, socio) VALUES (?, ?, ?, ?, ?)",
              (descripcion, importe, fecha, tipo, socio))
    conn.commit()

# Función para listar todos los ingresos
def listar_ingresos():
    datos = c.execute("SELECT * FROM INGRESOS")
    # df_ingresos = st.dataframe(datos)
    return datos #c.fetchall()

# Función para eliminar un ingreso por ID
def eliminar_ingreso(id):
    c.execute("DELETE FROM INGRESOS WHERE id=?", (id,))
    conn.commit()

# Crear la aplicación Streamlit
st.title("Sistema ABM de Ingresos")

# Sidebar
st.button("Listar Ingresos")

# if opcion == "Agregar Ingreso":
#     st.header("Agregar Ingreso")
#     descripcion = st.text_input("Descripción:")
#     importe = st.number_input("Importe:", min_value=0)
#     fecha = st.date_input("Fecha:", datetime.now())
#     tipo = st.selectbox("Tipo", ["Inversión Socio", "Ingreso Negocio", "Otro"])
#     socio = st.selectbox("Socio", ["Andy", "Adri", "Maxi", "Pablo"])
    
#     if st.button("Agregar"):
#         agregar_ingreso(descripcion, importe, fecha, tipo, socio)
#         st.success("Ingreso agregado exitosamente.")

# elif opcion == "Listar Ingresos":
st.header("Listar Ingresos")
ingresos = listar_ingresos()

# Mostrar la tabla de ingresos
for ingreso in ingresos:
    if st.checkbox(f"Eliminar Ingreso {ingreso[0]}"):
        eliminar_ingreso(ingreso[0])
        st.success(f"Ingreso {ingreso[0]} eliminado.")
    df_ingreso = pd.DataFrame(ingreso)
    df_ing = df_ingreso.T
    df_ing.columns=["ID", "Descripción", "Importe", "Fecha", "Tipo", "Socio"]
    st.table(df_ing)#st.write(f"ID: {ingreso[0]}, Descripción: {ingreso[1]}, Importe: {ingreso[2]}, Fecha: {ingreso[3]}, Tipo: {ingreso[4]}, Socio: {ingreso[5]}")
        

# Cerrar la conexión a la base de datos
conn.close()
