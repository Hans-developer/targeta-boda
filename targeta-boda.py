import streamlit as st
import pandas as pd
import os

# Nombre del archivo CSV
CSV_FILE = "invitados.csv"

# Función para cargar los datos
def cargar_datos():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Nombre"])

# Función para guardar los datos
def guardar_datos(nombre):
    df = cargar_datos()
    df = df.append({"Nombre": nombre}, ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# Título de la aplicación
st.title("Invitación de Boda")

# Información de la boda
st.header("¡Estás cordialmente invitado a nuestra boda!")
st.subheader("Fecha: 25 de diciembre de 2025")
st.subheader("Lugar: Jardines del Castillo, Santiago")

# Formulario para que los invitados ingresen sus nombres
st.markdown("### Por favor, ingresa tu nombre:")
nombre_invitado = st.text_input("Nombre del invitado")

# Botón para confirmar asistencia
if st.button("Confirmar asistencia"):
    if nombre_invitado:
        guardar_datos(nombre_invitado)
        st.success(f"{nombre_invitado}, tu asistencia ha sido confirmada.")
    else:
        st.error("Por favor, ingresa tu nombre.")

# Sección de inicio de sesión para el administrador
st.markdown("### Área de Administrador")
usuario = st.text_input("Usuario")
contrasena = st.text_input("Contraseña", type="password")

# Verifica las credenciales
if st.button("Iniciar sesión"):
    if usuario == "admin" and contrasena == "admin123":  # Cambia las credenciales según sea necesario
        st.success("Inicio de sesión exitoso.")
        
        # Mostrar lista de asistentes
        st.markdown("### Lista de asistentes:")
        asistentes = cargar_datos()
        if not asistentes.empty:
            st.write(asistentes)
        else:
            st.write("No hay asistentes confirmados todavía.")
    else:
        st.error("Usuario o contraseña incorrectos.")
