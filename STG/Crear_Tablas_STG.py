import pymysql

# Configuración de la conexión a la base de datos
timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="prone-2024-prone-2024.k.aivencloud.com",
    password= BD_paswaord,
    read_timeout=timeout,
    port=11108,
    user="avnadmin",
    write_timeout=timeout,
)

# Listado de sentencias SQL para crear las tablas con clave primaria
tables = [
    """
    CREATE TABLE Propiedades_STG (
        property_id INT PRIMARY KEY,
        address VARCHAR(255),
        description TEXT,
        created_at_date DATE,
        created_at_time TIME,
        deleted_at_date DATE,
        deleted_at_time TIME,
        expenses INT,
        floors_amount INT,
        surface DECIMAL(10, 2),
        total_surface DECIMAL(10, 2),
        roofed_surface DECIMAL(10, 2),
        real_address VARCHAR(255),
        publication_title VARCHAR(255),
        web_price BOOLEAN
    );
    """,
    """
    CREATE TABLE Sucursales_STG (
        branch_id INT PRIMARY KEY,
        branch_address VARCHAR(255),
        branch_alternative_phone BIGINT,
        branch_alternative_phone_area INT,
        branch_created_date DATE,
        branch_created_time TIME,
        property_id INT
    );
    """,
    """
    CREATE TABLE Ubicaciones_STG (
        location_id INT PRIMARY KEY,
        property_id INT,
        location_name VARCHAR(255),
        location_full TEXT
    );
    """,
    """
    CREATE TABLE Productores_STG (
        producer_id INT PRIMARY KEY,
        property_id INT,
        producer_name VARCHAR(255),
        producer_email VARCHAR(255),
        producer_phone VARCHAR(50)
    );
    """,
    """
    CREATE TABLE Tipos_Propiedades_STG (
        type_id INT PRIMARY KEY,
        property_id INT,
        type_name VARCHAR(255),
        type_code VARCHAR(50)
    );
    """,
    """
    CREATE TABLE Operaciones_STG (
        operation_id INT PRIMARY KEY,
        property_id INT,
        operation_type VARCHAR(50),
        price DECIMAL(15, 2),
        currency VARCHAR(10)
    );
    """,
    """
    CREATE TABLE Propietarios_STG (
        owner_id INT PRIMARY KEY,
        property_id INT,
        owner_name VARCHAR(255),
        owner_email VARCHAR(255),
        owner_phone VARCHAR(50),
        owner_work_email VARCHAR(255)
    );
    """
]

# Ejecución del script para crear las tablas
try:
    cursor = connection.cursor()
    for table in tables:
        cursor.execute(table)
        print("Tabla creada con éxito.")
finally:
    connection.close()
