import json
from pathlib import Path
from api.api_client import APIClient

datos = APIClient().obtener_registros(5)
print(json.dumps(datos, ensure_ascii=False, indent=4))
Path('evidencias').mkdir(exist_ok=True)
Path('evidencias/respuesta_api.json').write_text(json.dumps(datos, ensure_ascii=False, indent=4), encoding='utf-8')
