import streamlit as st

def main():
    # Título de la aplicación
    st.title("Contador de Palabras")

    # Campo de texto para ingresar el texto
    texto_usuario = st.text_area("Ingresa tu texto a continuación:")

    # Botón para contar las palabras
    if st.button("Contar palabras"):
        if texto_usuario.strip():  # Verifica que el texto no esté vacío
            # Divide el texto en palabras y las cuenta
            palabras = texto_usuario.split()
            numero_palabras = len(palabras)

            # Muestra el resultado
            st.success(f"El texto ingresado tiene {numero_palabras} palabras.")

            # Animación de globos
            st.balloons()
        else:
            st.warning("Por favor, ingresa un texto antes de presionar el botón.")

if __name__ == "__main__":
    main()
