import streamlit as st
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Crear la conexión a la base de datos (asegúrate de que esta parte esté antes de la función listar_ingresos)
conn = sqlite3.connect('db/bar.db')
c = conn.cursor()
st.set_option('deprecation.showPyplotGlobalUse', False)

# ...

# Función para listar ingresos por tipo
def ingresos_por_tipo():
    c.execute("SELECT tipo, SUM(importe), fecha FROM INGRESOS GROUP BY tipo")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=["Tipo", "Total","Fecha"])
    return df

def egresos_por_tipo():
    c.execute("SELECT tipo, SUM(importe), fecha FROM EGRESOS GROUP BY tipo")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=["Tipo", "Total","Fecha"])
    return df

# Crear la aplicación Streamlit
# Agregar una sección para mostrar gráficos
st.header("Gráficos")

# Gráfico de ingresos por tipo
st.subheader("Ingresos por Tipo")
df_tipo = ingresos_por_tipo()
fig, ax = plt.subplots()
ax.pie(df_tipo["Total"], labels=df_tipo["Tipo"], autopct='%1.1f%%', shadow=True, startangle=90)
    # (df_tipo["Tipo"], df_tipo["Total"])
ct = st.container()


fig.set_size_inches(1, 1)



st.pyplot(fig,clear_figure=True,use_container_width=True,facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False)

# ...

st.subheader("Egresos por Tipo")
df_tipo_eg = egresos_por_tipo()
fig, ax = plt.subplots()
ax.pie(df_tipo_eg["Total"], labels=df_tipo_eg["Tipo"], autopct='%1.1f%%', shadow=True, startangle=90)
    # (df_tipo["Tipo"], df_tipo["Total"])
ct = st.container()


fig.set_size_inches(1, 1)



st.pyplot(fig,clear_figure=True,use_container_width=True,facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False)

# Cerrar la conexión a la base de datos
conn.close()
