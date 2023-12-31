import streamlit as st
from egresos import Egresos
import pandas as pd
import sqlite3
from datetime import datetime

_descripcion = st.text_input("Descripcion")
_importe = st.number_input("Importe")
_fecha = st.date_input("Fecha", datetime.date(datetime.now()))
_time = st.time_input("Hora", datetime.time(datetime.now()))
_fecha = datetime.combine(_fecha, _time)
_tipo = st.selectbox("Tipo", ["General", "Gasto Materiales", "Adelanto"])# Socio", "Ingreso Negocio", "Otro"])
_destino = st.text_input("Destino")

if st.button("Guardar"):
    egreso = Egresos(_descripcion, _importe, _fecha, _tipo, _destino)
    egreso.guardar()
    st.success("Egreso guardado con exito")
    conn = sqlite3.connect("db/bar.db")
    c = conn.cursor()
    st.dataframe(pd.read_sql_query("SELECT * FROM EGRESOS", conn))
    conn.close()
    



