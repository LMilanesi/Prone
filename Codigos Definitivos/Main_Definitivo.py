import json
import pandas as pd

# Cargar el archivo JSON
with open('Json_Propiedades_Completo.json', 'r', encoding='utf-8') as file:
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
for obj in data:
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
        "reference_code": obj.get('reference_code', None),
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
        'web_price': obj.get('web_price', None),
        'age': obj.get('age', None),
        'bathroom_amount': obj.get('bathroom_amount', None),
        'custom1': obj.get('custom1', None),
        'custom_tags': obj.get('custom_tags', None),
        'deleted_at': obj.get('deleted_at', None),
        'depth_measure': obj.get('depth_measure', None),
        'description_only': obj.get('description_only', None),
        'development': obj.get('development', None),
        'development_excel_extra_data': obj.get('development_excel_extra_data', None),
        'disposition': obj.get('disposition', None),
        'extra_attributes': obj.get('extra_attributes', None),
        'fake_address': obj.get('fake_address', None),
        'footer': obj.get('footer', None),
        'front_measure': obj.get('front_measure', None),
        'geo_lat': obj.get('geo_lat', None),
        'geo_long': obj.get('geo_long', None),
        'gm_location_type': obj.get('gm_location_type', None),
        'has_temporary_rent': obj.get('has_temporary_rent', None),
        'internal_data': obj.get('internal_data', None),
        'is_denounced': obj.get('is_denounced', None),
        'is_starred_on_web': obj.get('is_starred_on_web', None),
        'legally_checked': obj.get('legally_checked', None),
        'occupation': obj.get('occupation', None),
        'orientation': obj.get('orientation', None),
        'parking_lot_amount': obj.get('parking_lot_amount', None),
        'producer': obj.get('producer', None),
        'property_condition': obj.get('property_condition', None),
        'public_url': obj.get('public_url', None),
        'rich_description': obj.get('rich_description', None),
        'room_amount': obj.get('room_amount', None),
        'semiroofed_surface': obj.get('semiroofed_surface', None),
        'situation': obj.get('situation', None),
        'status': obj.get('status', None),
        'suite_amount': obj.get('suite_amount', None),
        'surface_measurement': obj.get('surface_measurement', None),
        'tags': obj.get('tags', None),
        'toilet_amount': obj.get('toilet_amount', None),
        'transaction_requirements': obj.get('transaction_requirements', None),
        'unroofed_surface': obj.get('unroofed_surface', None),
        'videos': obj.get('videos', None),
        'zonification': obj.get('zonification', None)
    }
    property_rows.append(property_data)

    # Desanidar los datos de la sucursal (branch)
    branch = obj.get('branch', None)
    if branch:
        branch_created_date_time = branch.get('created_date', None)
        branch_created_date, branch_created_time = branch_created_date_time.split('T') if branch_created_date_time else (None, None)

        branch_data = {
            'property_id': obj.get('id', None),
            'branch_id': branch.get('id', None),
            'branch_address': branch.get('address', None),
            'branch_alternative_phone': branch.get('alternative_phone', None),
            'branch_alternative_phone_area': branch.get('alternative_phone_area', None),
            'branch_created_date': branch_created_date,
            'branch_created_time': branch_created_time,
            'branch_alternative_phone_country_code': branch.get('alternative_phone_country_code', None),
            'branch_alternative_phone_extension': branch.get('alternative_phone_extension', None),
            'branch_type': branch.get('branch_type', None),
            'contact_time': branch.get('contact_time', None),
            'display_name': branch.get('display_name', None),
            'email': branch.get('email', None),
            'geo_lat': branch.get('geo_lat', None),
            'geo_long': branch.get('geo_long', None),
            'gm_location_type': branch.get('gm_location_type', None),
            'is_default': branch.get('is_default', None),
            'logo': branch.get('logo', None),
            'name': branch.get('name', None),
            'pdf_footer_text': branch.get('pdf_footer_text', None),
            'phone': branch.get('phone', None),
            'phone_area': branch.get('phone_area', None),
            'phone_country_code': branch.get('phone_country_code', None),
            'phone_extension': branch.get('phone_extension', None),
            'use_pdf_footer': branch.get('use_pdf_footer', None)
        }
        branch_rows.append(branch_data)

    # Desanidar los datos de la ubicación (location)
    location = obj.get('location', None)
    if location:
        location_data = {
            'property_id': obj.get('id', None),
            'location_id': location.get('id', None),
            'location_name': location.get('name', None),
            'location_full': location.get('full_location', None),
            'location_short': location.get('short_location', None),
            'location_state': location.get('state', None),
            'location_weight': location.get('weight', None),
            'location_parent_division': location.get('parent_division', None),
            'location_divisions': location.get('divisions', [])
        }
        location_rows.append(location_data)

    # Desanidar datos del productor (producer)
    producer = obj.get('producer', None)
    if producer:
        producer_data = {
            'property_id': obj.get('id', None),
            'producer_id': producer.get('id', None),
            'producer_name': producer.get('name', None),
            'producer_email': producer.get('email', None),
            'producer_phone': producer.get('phone', None),
            'producer_cellphone': producer.get('cellphone', None),
            'producer_position': producer.get('position', None),
            'producer_picture': producer.get('picture', None)
        }
        producer_rows.append(producer_data)

    # Desanidar los datos del tipo de propiedad (type)
    type_info = obj.get('type', None)
    if type_info:
        type_data = {
            'property_id': obj.get('id', None),
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
                'property_id': obj.get('id', None),
                'operation_id': operation_id,
                'operation_type': operation_type,
                'price': price.get('price', None),
                'currency': price.get('currency', None),
                'period': price.get('period', None)
            }
            operation_rows.append(operation_data)

    # Desanidar y agregar los propietarios (property_owners)
    property_owners = obj.get('internal_data', {}).get('property_owners', [])
    for owner in property_owners:
        owner_data = {
            'property_id': obj.get('id', None),
            'owner_id': owner.get('id', None),
            'owner_name': owner.get('name', None),
            'owner_email': owner.get('email', None),
            'owner_phone': owner.get('cellphone', None),
            'owner_work_email': owner.get('work_email', None),
            'owner_birthdate': owner.get('birthdate', None),
            'owner_document_number': owner.get('document_number', None),
            'owner_other_email': owner.get('other_email', None),
            'owner_other_phone': owner.get('other_phone', None),
            'owner_created_at': owner.get('created_at', None),
            'owner_updated_at': owner.get('updated_at', None)
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
