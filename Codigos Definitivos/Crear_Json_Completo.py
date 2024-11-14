import requests
import json
import urllib.parse

# Base URL y Endpoint específico
base_url = "http://tokkobroker.com/api"
endpoint = "/v1/property/search/"

# Parámetros comunes para cada solicitud
params = {
    "lang": "es_ar",
    "key": "8c8e330d1213d990d7a1c5e568ecf82ebd240850",  # Tu API Key
    "data": '{"with_custom_tags":[],"current_localization_id":0,"current_localization_type":"country","price_from":0,"price_to":999999999,"operation_types":[1,2,3],"property_types":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24],"currency":"ANY","filters":[],"only_available":false,"append_available": "checked"}',
    "format": "json",
    "limit": 100  # Lotes de 100 propiedades
}

# Ruta de salida fija
output_file_path = r"C:\Users\renzo\Desktop\Trabajo Prone\Prone\Codigos Definitivos\Json_Propiedades_Completo.json"

# Variable para almacenar todas las propiedades
all_properties = []
offset = 0

# Obtener propiedades de manera paginada
while True:
    # Añadir el parámetro offset al conjunto de parámetros
    params["offset"] = offset

    # Construir la URL con los parámetros
    url = f"{base_url}{endpoint}?{urllib.parse.urlencode(params)}"

    try:
        # Realizar la solicitud GET a la URL
        response = requests.get(url)
        response.raise_for_status()  # Verificar si hubo errores

        # Parsear la respuesta en formato JSON
        data = response.json()

        # Revisar si se obtuvieron propiedades
        if "objects" in data and data["objects"]:
            all_properties.extend(data["objects"])
            offset += 100  # Incrementar el offset para el próximo lote
        else:
            break  # No hay más propiedades, salir del bucle

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        break

# Guardar todas las propiedades en un archivo JSON
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(all_properties, output_file, ensure_ascii=False, indent=4)

# Cargar el archivo JSON localmente para verificar el contenido
with open(output_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Verificar cuántas propiedades hay
num_properties = len(data) if isinstance(data, list) else len(data.get('objects', []))
print(f"Número de propiedades: {num_properties}")
