import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado requerido
st.header("Análisis Exploratorio de Vehículos")

# Cargar el dataset
df = pd.read_csv("vehicles_us.csv")

st.write("### Vista previa del dataset")
st.dataframe(df.head())

# Botón requerido por el proyecto para mostrar un histograma
if st.button("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50, title="Histograma de precios")
    st.plotly_chart(fig)

st.write("### Precio por Año del Vehículo")

if st.button("Mostrar gráfico de dispersión precio vs año"):
    fig2 = px.scatter(
        df,
        x="model_year",
        y="price",
        title="Precio por Año del Vehículo",
        trendline="ols"
    )
    st.plotly_chart(fig2)
    