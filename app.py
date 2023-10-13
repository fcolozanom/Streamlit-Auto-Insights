import pandas as pd
import plotly.express as px
import streamlit as st

# Agrega un encabezado
st.header('Análisis de datos de anuncios de venta de coches')

# Lee los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crea casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Si la casilla de verificación para el histograma está seleccionada
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')

    # Crea un histograma
    fig = px.histogram(car_data, x="odometer")

    # Muestra un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Si la casilla de verificación para el gráfico de dispersión está seleccionada
if build_scatter:
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')

    # Crea un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # Muestra un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
