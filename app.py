import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


# Cargar el conjunto de datos Iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
class_names = iris.target_names
feature_names = iris.feature_names


# Configuración de la aplicación
st.title("Aplicación de Streamlit para Visualizar Datos")
st.sidebar.title("Configuración")

# Selector de especies
selected_class = st.sidebar.selectbox("Selecciona una especie", class_names)

# Filtrar el conjunto de datos por la especie seleccionada
selected_data = iris_df[iris_df['target'] == class_names.tolist().index(selected_class)]

# Mostrar detalles de la especie seleccionada
st.write(f"Detalles de la especie seleccionada: {selected_class}")
st.write(selected_data.head())

# Visualización de datos (puedes personalizar esta sección según tus necesidades)
st.subheader("Visualización de Datos")
st.bar_chart(selected_data[iris.feature_names])

# Puedes agregar más visualizaciones según tus necesidades

st.subheader("Visualización de Datos")

# Gráfico de barras
fig, ax = plt.subplots()
selected_data[iris.feature_names].mean().plot(kind='bar', ax=ax)
ax.set_title(f"Promedio de Características para la especie {selected_class}")
ax.set_ylabel("Promedio")
ax.set_xlabel("Características")
st.pyplot(fig)