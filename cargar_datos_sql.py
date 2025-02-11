import sqlite3
import pandas as pd

conn = sqlite3.connect("sap_reports.db")
cursor = conn.cursor()

df = pd.read_excel("reporte_sap.xlsx")

for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO reportes_sap (fecha, cliente, region, metodo_pago, canal_venta, producto, cantidad, precio_unitario, total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (row["Fecha"], row["Cliente"], row["Región"], row["Método de Pago"], row["Canal de Venta"], row["Producto"], row["Cantidad"], row["Precio Unitario"], row["Total"]))

conn.commit()
conn.close()

print("✅ Datos insertados en la base de datos correctamente.")
