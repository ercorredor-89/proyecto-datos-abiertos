import os
import json
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def obtener_conexion():
    servidor = os.getenv('DB_SERVER')
    base = os.getenv('DB_NAME')
    driver = os.getenv('DB_DRIVER')
    cadena = f'DRIVER={{{driver}}};SERVER={servidor};DATABASE={base};TrustServerCertificate=yes;'
    if os.getenv('DB_TRUSTED', 'yes').lower() == 'yes':
        cadena += 'Trusted_Connection=yes;'
    else:
        cadena += f"UID={os.getenv('DB_USER')};PWD={os.getenv('DB_PASSWORD')};"
    return pyodbc.connect(cadena)

def guardar_registros(registros):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    insertados = 0
    try:
        for registro in registros:
            codigo = registro.get('cod_mpio')
            if not codigo:
                continue
            cursor.execute('SELECT id FROM dbo.RegistrosAPI WHERE id_api = ?', codigo)
            if cursor.fetchone() is None:
                cursor.execute('''INSERT INTO dbo.RegistrosAPI
                    (id_api, codigo_departamento, departamento, municipio, tipo, longitud, latitud, json_original)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', codigo, registro.get('cod_dpto'),
                    registro.get('dpto'), registro.get('nom_mpio'), registro.get('tipo_municipio'),
                    registro.get('longitud'), registro.get('latitud'), json.dumps(registro, ensure_ascii=False))
                insertados += 1
        conexion.commit()
        return insertados
    except Exception:
        conexion.rollback()
        raise
    finally:
        cursor.close()
        conexion.close()

def consultar_registros(filtro=''):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        consulta = 'SELECT TOP 100 id_api, codigo_departamento, departamento, municipio, tipo, longitud, latitud FROM dbo.RegistrosAPI'
        if filtro:
            consulta += ' WHERE municipio LIKE ? OR departamento LIKE ?'
            cursor.execute(consulta + ' ORDER BY id_api', f'%{filtro}%', f'%{filtro}%')
        else:
            cursor.execute(consulta + ' ORDER BY id_api')
        columnas = [columna[0] for columna in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    finally:
        cursor.close()
        conexion.close()

def contar_registros():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute('SELECT COUNT(*) FROM dbo.RegistrosAPI')
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        conexion.close()
