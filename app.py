import streamlit as st
from controller.controller import SalesDataController
import tempfile
import os

def main():
    st.title("Análise de Vendas")
    uploaded_file = st.file_uploader("Faça o upload do arquivo CSV", type=['csv'])

    if uploaded_file is not None:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar o arquivo: {str(e)}")
            return

        try:
            controller = SalesDataController(temp_file_path)
            controller.process_data()
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar os dados: {str(e)}")
            os.unlink(temp_file_path)

if __name__ == "__main__":
    main()
