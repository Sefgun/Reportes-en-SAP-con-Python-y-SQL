import sqlite3
import pandas as pd

conn = sqlite3.connect("sap_reports.db")

df = pd.read_sql_query("SELECT * FROM reportes_sap", conn)

conn.close()
print(df)
