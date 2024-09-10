import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la aplicación
st.title('Aplicación de Datos de Delitos')

# Definir los posibles valores para las columnas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C', 'Ciudad D']
delitos = ['Robo', 'Asalto', 'Vandalismo', 'Fraude']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Generar un dataset ficticio
np.random.seed(42)  # Para reproducibilidad
data = {
    'Ciudad': np.random.choice(ciudades, 50),
    'Hora del día': np.random.randint(0, 24, 50),
    'Día de la semana': np.random.choice(dias_semana, 50),
    'Tipo de delito': np.random.choice(delitos, 50)
}

df = pd.DataFrame(data)

# Sidebar para filtros
st.sidebar.header('segmentador')
selected_ciudad = st.sidebar.multiselect('Selecciona la ciudad', ciudades, default=ciudades)
selected_hora = st.sidebar.slider('Selecciona la hora del día', 0, 23, (0, 23))
selected_dia = st.sidebar.multiselect('Selecciona el día de la semana', dias_semana, default=dias_semana)

# Aplicar filtros al dataframe
filtered_df = df[
    (df['Ciudad'].isin(selected_ciudad)) &
    (df['Hora del día'].between(selected_hora[0], selected_hora[1])) &
    (df['Día de la semana'].isin(selected_dia))
]

st.write("### Dataset Filtrado")
st.write(filtered_df)

# Graficar la distribución de frecuencia de la ciudad
st.write("### Distribución de Frecuencia por Ciudad")
ciudad_counts = filtered_df['Ciudad'].value_counts()
plt.figure(figsize=(10, 5))
sns.barplot(x=ciudad_counts.index, y=ciudad_counts.values, palette='viridis')
plt.title('Número de Delitos por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Número de Delitos')
st.pyplot(plt.gcf())
plt.clf()

# Graficar la distribución de frecuencia de los tipos de delito
st.write("### Distribución de Frecuencia por Tipo de Delito")
delito_counts = filtered_df['Tipo de delito'].value_counts()
plt.figure(figsize=(10, 5))
sns.barplot(x=delito_counts.index, y=delito_counts.values, palette='viridis')
plt.title('Número de Delitos por Tipo')
plt.xlabel('Tipo de Delito')
plt.ylabel('Número de Delitos')
st.pyplot(plt.gcf())
plt.clf()

# Graficar la distribución de tipos de delito por día de la semana
st.write("### Tipo de Delito por Día de la Semana")
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_df, x='Día de la semana', hue='Tipo de delito', palette='viridis')
plt.title('Número de Delitos por Día de la Semana y Tipo')
plt.xlabel('Día de la Semana')
plt.ylabel('Número de Delitos')
plt.legend(title='Tipo de Delito')
st.pyplot(plt.gcf())
plt.clf()

