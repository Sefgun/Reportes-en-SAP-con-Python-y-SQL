import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect("sap_reports.db")

# Leer los datos de la tabla
df = pd.read_sql_query("SELECT * FROM reportes_sap", conn)

# Cerrar la conexión
conn.close()

# Mostrar los datos
print(df)
