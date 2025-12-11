# Tripletenprojectdashboard

Este proyecto es un panel interactivo construido con Streamlit para explorar un conjunto de datos de anuncios de vehículos usados (`vehicles_us.csv`).

La aplicación permite:

- Ver una muestra del conjunto de datos en una tabla interactiva.
- Generar, mediante un botón, un histograma de los precios de los vehículos usando Plotly Express.
- Generar, mediante otro botón, un gráfico de dispersión del precio en función del año del vehículo, con una línea de tendencia.
- Complementar el análisis usando el notebook de análisis exploratorio `notebooks/EDA.ipynb`.

## Cómo ejecutar la aplicación localmente

```bash
python -m venv .venv        # crear entorno virtual (si no existe)
source .venv/bin/activate   # activar entorno virtual
pip install -r requirements.txt
streamlit run app.py

