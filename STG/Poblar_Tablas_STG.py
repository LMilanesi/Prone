import pymysql
import pandas as pd
import numpy as np

# Configuración de la conexión a la base de datos
timeout = 10 
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="prone-2024-prone-2024.k.aivencloud.com",
    password= pasword,
    read_timeout=timeout,
    port=11108,
    user="avnadmin",
    write_timeout=timeout,
)

# Leer el archivo Excel
file_path = r'C:\Users\Lauta\OneDrive\Escritorio\Prone\Carga Inicial\Propiedades_Todo_en_Uno_NoDispo.xlsx'  

# Función para insertar datos en una tabla
def insert_into_table(cursor, table_name, df):
    cols = ",".join([f"`{col}`" for col in df.columns])
    placeholders = ",".join(["%s"] * len(df.columns))
    insert_stmt = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    data = [tuple(row) for row in df.values]
    cursor.executemany(insert_stmt, data)

# Ejecución del script para insertar datos
try:
    cursor = connection.cursor()

    # Cargar datos de cada hoja y hacer la inserción en la base de datos
    hojas_y_tablas = {
        "Propiedades": "Propiedades_STG",
        "Sucursales": "Sucursales_STG",
        "Ubicaciones": "Ubicaciones_STG",
        "Productores": "Productores_STG",
        "Tipos_Propiedades": "Tipos_Propiedades_STG",
        "Operaciones": "Operaciones_STG",
        "Propietarios": "Propietarios_STG"
    }

    for hoja, tabla in hojas_y_tablas.items():
        if hoja == "Propiedades":  # Solo queremos poblar la tabla 'Propiedades_STG'
            df = pd.read_excel(file_path, sheet_name=hoja)

            # Reemplazar NaN por None (que se convierte en NULL en MySQL)
            df = df.replace({np.nan: None})

            insert_into_table(cursor, tabla, df)
            connection.commit()
            print(f"Datos insertados correctamente en la tabla {tabla}.")

finally:
    connection.close()


import pymysql
import pandas as pd
import numpy as np

# Configuración de la conexión a la base de datos
timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="prone-2024-prone-2024.k.aivencloud.com",
    password= pasword,
    read_timeout=timeout,
    port=11108,
    user="avnadmin",
    write_timeout=timeout,
)

# Leer el archivo Excel
file_path = r'C:\Users\Lauta\OneDrive\Escritorio\Prone\Carga Inicial\Propiedades_Todo_en_Uno_NoDispo.xlsx'  

# Función para insertar datos en una tabla
def insert_into_table(cursor, table_name, df):
    cols = ",".join([f"`{col}`" for col in df.columns])
    placeholders = ",".join(["%s"] * len(df.columns))
    insert_stmt = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    data = [tuple(row) for row in df.values]
    cursor.executemany(insert_stmt, data)

# Ejecución del script para insertar datos
try:
    cursor = connection.cursor()

    # Cargar datos de cada hoja y hacer la inserción en la base de datos
    hojas_y_tablas = {
        "Sucursales": "Sucursales_STG",
        "Ubicaciones": "Ubicaciones_STG",
        "Productores": "Productores_STG",
        "Tipos_Propiedades": "Tipos_Propiedades_STG",
        "Operaciones": "Operaciones_STG",
        "Propietarios": "Propietarios_STG"
    }

    for hoja, tabla in hojas_y_tablas.items():
        df = pd.read_excel(file_path, sheet_name=hoja)

        # Reemplazar NaN por None (que se convierte en NULL en MySQL)
        df = df.replace({np.nan: None})

        insert_into_table(cursor, tabla, df)
        connection.commit()
        print(f"Datos insertados correctamente en la tabla {tabla}.")

finally:
    connection.close()
