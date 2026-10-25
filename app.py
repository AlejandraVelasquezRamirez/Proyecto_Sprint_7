import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header('Panel de control de anuncios de venta de coches')

# --- 1. SECCIÓN DEL HISTOGRAMA ---
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de'
        ' venta de coches'
    )

    # Crear el histograma con plotly.graph_objects usando la columna 'odometer'
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)


# --- 2. SECCIÓN DEL GRÁFICO DE DISPERSIÓN ---
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de'
        ' anuncios de venta de coches'
    )

    # Crear el gráfico de dispersión (por ejemplo: odómetro vs precio)
    fig_scatter = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers',
                marker=dict(color='blue', opacity=0.5),
            )
        ]
    )
    fig_scatter.update_layout(title_text='Precio vs. Odómetro')

    # Mostrar el gráfico de dispersión en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
