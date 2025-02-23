#
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mode

# Configurar el diseño de la app
st.title("📊 Análisis Estadístico de Datos Cuantitativos")
st.markdown("Introduce una lista de números separados por `;` y obtendrás un análisis estadístico completo.")

# Entrada de datos
input_data = st.text_area("📥 Ingresa los datos:", "12.5; 15.8; 20.3; 22.1; 18.4")

# Función para validar datos y convertirlos en una lista de números
def procesar_datos(input_text):
    try:
        # Convertir texto en lista de números
        valores = list(map(float, input_text.replace(",", ".").split(";")))
        
        # Verificar si hay al menos dos valores
        if len(valores) < 2:
            st.error("⚠️ Se requieren al menos dos valores numéricos para el análisis.")
            return None
        return valores
    except ValueError:
        st.error("⚠️ Error: Solo se permiten números separados por `;`.")
        return None

# Procesar la entrada
datos = procesar_datos(input_data)

if datos:
    # Convertir a DataFrame para análisis
    df = pd.DataFrame({"Valores": datos})

    # Calcular estadísticas
    media = np.mean(datos)
    moda = mode(datos, keepdims=True).mode[0]
    mediana = np.median(datos)
    desviacion_std = np.std(datos, ddof=1)
    coef_variacion = (desviacion_std / media) * 100

    # Mostrar estadísticas en tabla
    st.subheader("📋 Estadísticas Generales")
    st.table(pd.DataFrame({
        "Estadística": ["Promedio", "Moda", "Mediana", "Desviación Estándar", "Coef. Variación (%)"],
        "Valor": [f"{media:.2f}", f"{moda:.2f}", f"{mediana:.2f}", f"{desviacion_std:.2f}", f"{coef_variacion:.2f}"]
    }))

    # Generar gráficos
    st.subheader("📊 Visualización de Datos")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Histograma
    sns.histplot(df, x="Valores", bins=10, kde=True, ax=axes[0], color="blue")
    axes[0].set_title("Histograma")

    # Boxplot
    sns.boxplot(data=df, x="Valores", ax=axes[1], color="orange")
    axes[1].set_title("Boxplot")

    st.pyplot(fig)

