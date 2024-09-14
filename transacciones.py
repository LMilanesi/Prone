import pandas as pd

# Crear un DataFrame con la estructura solicitada
transacciones = pd.DataFrame({
    'ID_Tokko': pd.Series(dtype='int'),
    'Direccion': pd.Series(dtype='str'),
    'Ciudad': pd.Series(dtype='str'),
    'Barrio': pd.Series(dtype='str'),
    'Tipo_Propiedad': pd.Series(dtype='str'),
    'Tipo_Contacto': pd.Series(dtype='str'),
    'Nombre_Cliente': pd.Series(dtype='str'),
    'Tipo_Cliente': pd.Series(dtype='str'),
    'Compartida': pd.Series(dtype='str'),
    'Precio_Publicacion_USD': pd.Series(dtype='float'),
    'Precio_Cierre_USD': pd.Series(dtype='float'),
    'Com_Total_USD': pd.Series(dtype='float'),
    'Com_PRONE_USD': pd.Series(dtype='float'),
    'Com_agente_USD': pd.Series(dtype='float'),
    'Apodo_Agente': pd.Series(dtype='str'),
    'Fecha_Reserva': pd.Series(dtype='datetime64[ns]'),
    'Fecha_Firma': pd.Series(dtype='datetime64[ns]'),
    'IVA_agente': pd.Series(dtype='float'),
    'IVA_o_Seña': pd.Series(dtype='float')
})

import pyodbc
import pandas as pd

# Parámetros de conexión
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=LMILADESKTOP\\SQLEXPRESS;'
    'DATABASE=PRONE_INT;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

# Crear el cursor
cursor = conn.cursor()



