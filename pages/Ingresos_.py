import streamlit as st
from ingresos import Ingresos
import pandas as pd
import sqlite3

_descripcion = st.text_input("Descripcion")
_importe = st.number_input("Importe")
_fecha = st.date_input("Fecha")
_tipo = st.selectbox("Tipo", ["Inversión Socio", "Ingreso Negocio", "Otro"])
_socio = st.selectbox("Socio", ["Andy", "Adri", "Maxi", "Pablo"])

if st.button("Guardar"):
    ingreso = Ingresos(_descripcion, _importe, _fecha, _tipo, _socio)
    ingreso.guardar()
    st.success("Ingreso guardado con exito")
    conn = sqlite3.connect("db/bar.db")
    c = conn.cursor()
    st.dataframe(pd.read_sql_query("SELECT * FROM INGRESOS", conn))
    conn.close()
    



