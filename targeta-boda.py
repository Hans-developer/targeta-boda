  import streamlit as st
import sqlite3
import os

# Nombre de la base de datos SQLite
DB_FILE = "invitados.db"

# Función para crear la tabla si no existe
def crear_tabla():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS invitados
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)""")
    conn.commit()
    conn.close()

# Función para guardar los datos de un invitado
def guardar_invitado(nombre):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO invitados (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

# Función para obtener la lista de invitados
def obtener_invitados():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM invitados")
    invitados = c.fetchall()
    conn.close()
    return invitados

# Función para eliminar un invitado
def eliminar_invitado(id_invitado):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM invitados WHERE id = ?", (id_invitado,))
    conn.commit()
    conn.close()

# Crear la tabla si no existe
crear_tabla()

# Sidebar para iniciar sesión
st.sidebar.title("Iniciar Sesión")
usuario = st.sidebar.text_input("Usuario")
contrasena = st.sidebar.text_input("Contraseña", type="password")

# Verificar las credenciales
if st.sidebar.button("Iniciar sesión"):
    if usuario == "admin" and contrasena == "admin123":
        st.sidebar.success("Inicio de sesión exitoso.")
        
        # Mostrar lista de asistentes y opción de eliminar
        st.sidebar.markdown("### Lista de asistentes:")
        invitados = obtener_invitados()
        if invitados:
            for invitado in invitados:
                id_invitado, nombre = invitado
                st.sidebar.write(f"{nombre}")
                if st.sidebar.button(f"Eliminar {nombre}", key=id_invitado):
                    eliminar_invitado(id_invitado)
                    st.experimental_rerun()
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

# Formulario para que los invitados ingresen su nombre completo
st.markdown("### Por favor, ingresa tu nombre completo:")
nombre_completo = st.text_input("Nombre completo del invitado")

# Botón para confirmar asistencia
if st.button("Registrar asistencia"):
    if nombre_completo:
        guardar_invitado(nombre_completo)
        st.success("Registro exitoso, ¡nos vemos en mi boda! Posdata: Marcela")
        nombre_completo = "" # Limpiar el campo después del registro exitoso
    else:
        st.error("Por favor, ingresa tu nombre completo.")
