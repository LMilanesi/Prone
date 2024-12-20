import json
import pandas as pd

# import pymysql

# timeout = 10
# connection = pymysql.connect(
#   charset="utf8mb4",
#   connect_timeout=timeout,
#   cursorclass=pymysql.cursors.DictCursor,
#   db="defaultdb",
#   host="prone-2024-prone-2024.k.aivencloud.com",
#   password= DB_PASSWORD,
#   read_timeout=timeout,
#   port=11108,
#   user="avnadmin",
#   write_timeout=timeout,
# )

# Cargar el archivo JSON
with open('Propiedades.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Crear listas para almacenar los datos separados
property_rows = []
branch_rows = []
location_rows = []
producer_rows = []
type_rows = []
operation_rows = []
owner_rows = []

# Recorrer cada objeto en la lista 'objects' del JSON
for obj in data.get('objects', []):
    # Datos principales de la propiedad
    created_at = obj.get('created_at', None)
    deleted_at = obj.get('deleted_at', None)
    
    # Dividir la fecha y la hora si los campos existen
    if created_at:
        created_at_date, created_at_time = created_at.split('T')
    else:
        created_at_date, created_at_time = None, None

    if deleted_at:
        deleted_at_date, deleted_at_time = deleted_at.split('T')
    else:
        deleted_at_date, deleted_at_time = None, None
    
    property_data = {
        'property_id': obj.get('id', None),
        "reference_code" : obj.get('reference_code', None),
        'address': obj.get('address', None),
        'description': obj.get('description', None),
        'created_at_date': created_at_date,  # Solo la fecha
        'created_at_time': created_at_time,  # Solo la hora
        'deleted_at_date': deleted_at_date,  # Solo la fecha
        'deleted_at_time': deleted_at_time,  # Solo la hora
        'expenses': obj.get('expenses', None),
        'floors_amount': obj.get('floors_amount', None),
        'surface': obj.get('surface', None),
        'total_surface': obj.get('total_surface', None),
        'roofed_surface': obj.get('roofed_surface', None),
        'real_address': obj.get('real_address', None),
        'publication_title': obj.get('publication_title', None),
        'web_price': obj.get('web_price', None)
    }
    property_rows.append(property_data)

    # Desanidar los datos de la sucursal (branch)
    branch = obj.get('branch', {})
    branch_created_date_time = branch.get('created_date', None)
    
    # Dividir la fecha y la hora si el campo existe
    if branch_created_date_time:
        branch_created_date, branch_created_time = branch_created_date_time.split('T')
    else:
        branch_created_date, branch_created_time = None, None
    
    branch_data = {
        'property_id': obj.get('id', None)  ,# Relacionar con propiedad
        'branch_id': branch.get('id', None),
        'branch_address': branch.get('address', None),
        'branch_alternative_phone': branch.get('alternative_phone', None),
        'branch_alternative_phone_area': branch.get('alternative_phone_area', None),
        'branch_created_date': branch_created_date,  # Solo la fecha
        'branch_created_time': branch_created_time # Solo la hora
        
    }
    branch_rows.append(branch_data)

    # Desanidar los datos de la ubicación (location)
    location = obj.get('location', {})
    location_data = {
        'property_id': obj.get('id', None), # Relacionar con propiedad
        'location_id': location.get('id', None),
        'location_name': location.get('name', None),
        'location_full': location.get('full_location', None)
    }
    location_rows.append(location_data)

    # Desanidar datos del productor (producer)
    producer = obj.get('producer', {})
    producer_data = {
         'property_id': obj.get('id', None),# Relacionar con propiedad
        'producer_id': producer.get('id', None),
        'producer_name': producer.get('name', None),
        'producer_email': producer.get('email', None),
        'producer_phone': producer.get('phone', None),
    }
    producer_rows.append(producer_data)

    # Desanidar los datos del tipo de propiedad (type)
    type_info = obj.get('type', {})
    type_data = {
        'property_id': obj.get('id', None) , # Relacionar con propiedad
        'type_id': type_info.get('id', None),
        'type_name': type_info.get('name', None),
        'type_code': type_info.get('code', None)
        
    }
    type_rows.append(type_data)

    # Desanidar las operaciones (operations) y precios
    operations = obj.get('operations', [])
    for operation in operations:
        operation_id = operation.get('operation_id', None)
        operation_type = operation.get('operation_type', None)
        for price in operation.get('prices', []):
            operation_data = {
                 'property_id': obj.get('id', None),  # Relacionar con propiedad
                'operation_id': operation_id,
                'operation_type': operation_type,
                'price': price.get('price', None),
                'currency': price.get('currency', None)
               
            }
            operation_rows.append(operation_data)

    # Desanidar y agregar los propietarios (property_owners)
    property_owners = obj.get('internal_data', {}).get('property_owners', [])
    for owner in property_owners:
        owner_data = {
             'property_id': obj.get('id', None),  # Relacionar con propiedad
            'owner_id': owner.get('id', None),
            'owner_name': owner.get('name', None),
            'owner_email': owner.get('email', None),
            'owner_phone': owner.get('cellphone', None),
            'owner_work_email': owner.get('work_email', None)
           
        }
        owner_rows.append(owner_data)

# Crear DataFrames separados
df_properties = pd.DataFrame(property_rows)
df_branch = pd.DataFrame(branch_rows)
df_location = pd.DataFrame(location_rows)
df_producer = pd.DataFrame(producer_rows)
df_type = pd.DataFrame(type_rows)
df_operations = pd.DataFrame(operation_rows)
df_owners = pd.DataFrame(owner_rows)

# Exportar todas las tablas a un solo archivo Excel con diferentes hojas
with pd.ExcelWriter('Propiedades_Todo_en_Uno.xlsx') as writer:
    df_properties.to_excel(writer, sheet_name='Propiedades', index=False)
    df_branch.to_excel(writer, sheet_name='Sucursales', index=False)
    df_location.to_excel(writer, sheet_name='Ubicaciones', index=False)
    df_producer.to_excel(writer, sheet_name='Productores', index=False)
    df_type.to_excel(writer, sheet_name='Tipos_Propiedades', index=False)
    df_operations.to_excel(writer, sheet_name='Operaciones', index=False)
    df_owners.to_excel(writer, sheet_name='Propietarios', index=False)

print("Datos exportados a un solo archivo Excel con hojas múltiples.")

