@echo off

:: Instalar las dependencias necesarias
pip install -r requirements.txt

:: Ejecutar la aplicación de Streamlit
streamlit run streamlit_app.py
