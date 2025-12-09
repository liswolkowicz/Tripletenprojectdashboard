import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Vehículos en Venta")

# Cargar el dataset
df = pd.read_csv("vehicles_us.csv")

st.write("### Vista previa de los datos")
st.dataframe(df.head())

# Histograma de precios
st.write("### Distribución de precios")
fig_price = px.histogram(df, x="price", nbins=50)
st.plotly_chart(fig_price)

# Scatter: año vs precio
st.write("### Precio en función del año del vehículo")
fig_year_price = px.scatter(df, x="model_year", y="price", trendline="ols")
st.plotly_chart(fig_year_price)

# Selección por fabricante
if "manufacturer" in df.columns:
    st.write("### Precios por fabricante")
    makers = df["manufacturer"].dropna().unique()
    choice = st.selectbox("Elige fabricante", makers)
    filtered = df[df["manufacturer"] == choice]
    fig_maker = px.box(filtered, x="manufacturer", y="price", title=f"Precios para {choice}")
    st.plotly_chart(fig_maker)

st.write("Dashboard construido con Streamlit, pandas y plotly-express.")