import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect("sap_reports.db")
cursor = conn.cursor()

# Crear la tabla con todas las columnas necesarias
cursor.execute('''
    CREATE TABLE reportes_sap (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        cliente TEXT,
        region TEXT,
        metodo_pago TEXT,
        canal_venta TEXT,
        producto TEXT,
        cantidad INTEGER,
        precio_unitario REAL,
        total REAL
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos creada con las nuevas columnas.")
