from models.datos_model import obtener_conexion
conexion = obtener_conexion()
print('Conexión exitosa a SQL Server')
conexion.close()
