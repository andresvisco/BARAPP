import streamlit as st
import sqlite3
import pandas as pd


conn = sqlite3.connect("db/bar.db")

c = conn.cursor()
df = pd.read_sql_query("SELECT * FROM INGRESOS", conn)

# st.dataframe(pd.read_sql_query("SELECT * FROM INGRESOS", conn))

# if key_name in st.session_state:
#     st.write(st.session_state[key_name]["deleted_rows"])
st.text("Listado de Ingresos")
st.dataframe(df)

st.text("Listado de Egresos")
df = pd.read_sql_query("SELECT * FROM EGRESOS", conn)
st.dataframe(df)

conn.close()


