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

# Sidebar para iniciar sesión
st.sidebar.title("Iniciar Sesión")
usuario = st.sidebar.text_input("Usuario")
contrasena = st.sidebar.text_input("Contraseña", type="password")

# Verifica las credenciales
if st.sidebar.button("Iniciar sesión"):
    if usuario == "admin" and contrasena == "admin123":  # Cambia las credenciales según sea necesario
        st.sidebar.success("Inicio de sesión exitoso.")
        
        # Mostrar lista de asistentes
        st.sidebar.markdown("### Lista de asistentes:")
        asistentes = cargar_datos()
        if not asistentes.empty:
            st.sidebar.write(asistentes)
            st.sidebar.write(f"Total de invitados registrados: {len(asistentes)}")
        else:
            st.sidebar.write("No hay asistentes confirmados todavía.")
    else:
        st.sidebar.error("Usuario o contraseña incorrectos.")

# Título de la aplicación
st.title("Registro para la Boda")

# Información de la boda
st.header("¡Estás cordialmente invitado a nuestra boda!")
st.subheader("Fecha: 25 de diciembre de 2025")
st.subheader("Lugar: Jardines del Castillo, Santiago")

# Formulario para que los invitados ingresen sus nombres
st.markdown("### Por favor, ingresa tu nombre:")
nombre_invitado = st.text_input("Nombre del invitado")

# Botón para confirmar asistencia
if st.button("Registrar asistencia"):
    if nombre_invitado:
        guardar_datos(nombre_invitado)
        st.success("Registro exitoso, ¡nos vemos en mi boda! Posdata: Marcela")
        st.experimental_rerun()  # Limpiar los campos y reiniciar la aplicación
    else:
        st.error("Por favor, ingresa tu nombre.")
