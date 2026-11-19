import os
from flask import Flask, render_template, request, redirect, url_for, flash
from api.api_client import APIClient
from models.datos_model import guardar_registros, consultar_registros, contar_registros

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave-local-municipios')

@app.route('/')
def inicio():
    filtro = request.args.get('q', '').strip()
    try:
        registros = consultar_registros(filtro)
        total = contar_registros()
    except Exception as error:
        flash(f'Error al consultar SQL Server: {error}')
        registros = []
        total = None
    return render_template('index.html', registros=registros, filtro=filtro, total=total)

@app.route('/sincronizar', methods=['POST'])
def sincronizar():
    try:
        datos = APIClient().obtener_registros(100)
        cantidad = guardar_registros(datos)
        flash(f'Nuevos registros guardados: {cantidad}')
    except Exception as error:
        flash(f'Error al sincronizar: {error}')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
