
# Sistema de consulta de municipios de Colombia

## Integrantes

- Moises López
- Edgar Corredor
- Sayra Alvarado

## Descripción del proyecto

El proyecto consiste en una aplicación web que permite consultar información de los municipios de Colombia mediante una API de Datos Abiertos. Los datos obtenidos se almacenan en SQL Server y se muestran en una página web desarrollada con Flask.

## Tecnologías utilizadas

- Python
- Flask
- SQL Server
- HTML
- CSS
- JSON
- Git
- GitHub

## Arquitectura MVC

- Modelo: permite la conexión con SQL Server, el almacenamiento y la consulta de los registros.
- Vista: muestra los registros almacenados mediante una página HTML.
- Controlador: recibe las solicitudes del usuario y conecta el modelo con la vista mediante Flask.

## Distribución de responsabilidades

### Integrante 1 - Moises López

- Consumo de la API de Datos Abiertos.
- Obtención de los datos en formato JSON.
- Identificación de los campos de la API.

### Integrante 2 - Edgar Corredor

- Creación de la base de datos DatosAbiertosDB.
- Creación de la tabla RegistrosAPI.
- Adaptación de las columnas.
- Conexión de Python con SQL Server.
- Almacenamiento y consulta de los registros.
- Validación de registros duplicados.

### Integrante 3 - Sayra Alvarado

- Desarrollo de la aplicación web con Flask.
- Conexión del controlador con el modelo.
- Diseño de la interfaz con HTML y CSS.
- Visualización de los registros y filtros de búsqueda.

## Funcionamiento

La aplicación consulta 100 registros de la API de Datos Abiertos DIVIPOLA del DANE. Los registros se guardan en SQL Server, evitando almacenar códigos de municipios duplicados.

La página web permite consultar los registros almacenados, realizar búsquedas por municipio o departamento y visualizar la cantidad total de registros y los resultados de cada búsqueda.

## Instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir el proyecto en Visual Studio Code.
3. Crear el entorno virtual con python -m venv venv.
4. Activar el entorno virtual.
5. Instalar las dependencias con pip install -r requirements.txt.
6. Ejecutar el archivo base_datos.sql en SQL Server.
7. Crear el archivo .env utilizando .env.example como referencia.
8. Configurar los datos de conexión a SQL Server.
9. Ejecutar python app.py.
10. Abrir http://127.0.0.1:5000 en el navegador.

## Resultados de las pruebas

- Consumo correcto de la API.
- Conexión exitosa con SQL Server.
- 100 registros almacenados.
- 100 registros únicos.
- 0 registros duplicados.
- Búsqueda por municipio.
- Búsqueda por departamento.
- Validación de búsquedas sin coincidencias.
- Visualización del resumen numérico.

## Evidencias

Las capturas de las pruebas realizadas se encuentran en la carpeta evidencias del repositorio.

[Consultar evidencias](./evidencias/)

## Conclusión

Con este proyecto se aplicaron los conocimientos adquiridos durante la asignatura, realizando la integración de una API, una base de datos SQL Server y una aplicación web con Python y Flask mediante la arquitectura MVC.
