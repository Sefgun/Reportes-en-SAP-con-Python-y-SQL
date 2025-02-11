import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de productos simulados
productos = ["Monitor", "Teclado", "Mouse", "Laptop", "Impresora", "Escritorio", "Silla"]
clientes = ["Empresa A", "Empresa B", "Empresa C", "Empresa D"]
regiones = ["Santiago", "Valparaíso", "Concepción", "Antofagasta"]
metodos_pago = ["Crédito", "Débito", "Transferencia"]
canales_venta = ["Online", "Tienda Física"]

# Generar datos simulados
datos = []
for _ in range(200):  # Más registros
    fecha = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 30))  
    producto = random.choice(productos)
    cliente = random.choice(clientes)
    region = random.choice(regiones)
    metodo_pago = random.choice(metodos_pago)
    canal_venta = random.choice(canales_venta)
    cantidad = random.randint(1, 10)
    precio_unitario = round(random.uniform(20, 500), 2)
    total = round(cantidad * precio_unitario, 2)
    datos.append([fecha.strftime("%d/%m/%Y"), cliente, region, metodo_pago, canal_venta, producto, cantidad, precio_unitario, total])

# Crear DataFrame
df = pd.DataFrame(datos, columns=["Fecha", "Cliente", "Región", "Método de Pago", "Canal de Venta", "Producto", "Cantidad", "Precio Unitario", "Total"])

# Guardar en Excel
df.to_excel("reporte_sap_completo.xlsx", index=False)

print("✅ Reporte SAP con más datos generado exitosamente.")
