import sqlite3

conn = sqlite3.connect("sap_reports.db")
cursor = conn.cursor()

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

conn.commit()
conn.close()

print("✅ Base de datos creada con las nuevas columnas.")
