# Sistema web de consulta de municipios de Colombia

## Objetivo
Consultar datos abiertos de Colombia, almacenar registros en SQL Server y mostrarlos en una página web con un buscador y un resumen de cantidades.

## Datos utilizados
Usamos DIVIPOLA- Códigos municipios, del DANE. Contiene códigos y nombres de municipios y departamentos, tipo y coordenadas.

Ficha: https://www.datos.gov.co/Mapas-Nacionales/DIVIPOLA-C-digos-municipios/gdxc-w37w

Endpoint: https://www.datos.gov.co/resource/gdxc-w37w.json?$limit=100&$order=cod_mpio%20ASC

| Campo API | Columna SQL | Descripción |
|---|---|---|
| cod_mpio | id_api | Código único del municipio |
| cod_dpto | codigo_departamento | Código del departamento |
| dpto | departamento | Nombre del departamento |
| nom_mpio | municipio | Nombre del municipio |
| tipo_municipio | tipo | Tipo de entidad territorial |
| longitud | longitud | Coordenada de longitud |
| latitud | latitud | Coordenada de latitud |

Los códigos se guardan como texto para conservar los ceros iniciales. También guardamos el JSON original y la fecha de captura. La columna id_api es única para evitar duplicados.

## Requisitos
Python 3.10 o superior, VS Code, SQL Server, SSMS, ODBC Driver 18 y conexión a Internet.

## Instalación y ejecución
1. Abrir la carpeta en VS Code.
2. Conectarse a SQL Server en SSMS y ejecutar base_datos.sql completo.
3. En PowerShell ejecutar:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

4. Editar .env con el nombre del servidor que se usa en SSMS. Si se usa autenticación SQL, cambiar DB_TRUSTED a no y completar usuario y contraseña. No publicar .env.
5. Ejecutar:

```powershell
.\venv\Scripts\python.exe probar_api.py
.\venv\Scripts\python.exe probar_conexion.py
.\venv\Scripts\python.exe app.py
```

6. Abrir http://127.0.0.1:5000 y pulsar el botón de sincronización. Buscar MEDELLÍN o ANTIOQUIA. La carga se limita a los primeros 100 registros ordenados por código, no a todo el país.

## Funcionamiento y MVC
- Servicio API: api/api_client.py recibe los datos JSON mediante requests.
- Modelo: models/datos_model.py conecta Python con SQL Server, guarda y consulta los registros.
- Controlador: app.py recibe las solicitudes, llama al servicio y al modelo y envía resultados a la vista.
- Vista: templates/index.html presenta los registros, el buscador y el total. static/estilos.css contiene los estilos.

El usuario pulsa sincronizar, Flask consulta la API, el modelo guarda los registros nuevos y la página muestra los datos almacenados. El buscador consulta SQL Server, no la API.

## Distribución de aportes
- Integrante 1 (completar nombre): selección de datos, API y evidencia JSON.
- Edgar Corredor: base de datos, conexión Python con SQL Server, inserción sin duplicados y consultas.
- Sayra Alvarado: controlador Flask, vista HTML, estilos y presentación de registros.
- Todos: integración, pruebas y documentación.

La distribución corresponde a las responsabilidades asignadas; confirmar los aportes reales antes de entregar.

## Pruebas y evidencias
Ejecutar las pruebas siguientes y guardar las capturas en evidencias/.

| Prueba | Resultado esperado |
|---|---|
| API | JSON con cinco registros |
| Conexión | Mensaje de conexión exitosa |
| Primera sincronización | Hasta 100 registros nuevos |
| Segunda sincronización | Cero nuevos si la fuente no cambió |
| Búsqueda | Coincidencias por municipio o departamento |
| Consulta SQL | Registros guardados y sin códigos repetidos |

En SSMS ejecutar:

```sql
USE DatosAbiertosDB;
SELECT * FROM dbo.RegistrosAPI;
SELECT COUNT(*) AS total FROM dbo.RegistrosAPI;
SELECT id_api, COUNT(*) AS cantidad FROM dbo.RegistrosAPI GROUP BY id_api HAVING COUNT(*) > 1;
```

La última consulta debe devolver cero filas. Las pruebas reales y capturas se deben realizar en el equipo con SQL Server instalado.
