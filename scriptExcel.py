import sqlite3
import pandas as pd

# Ruta al archivo SQLite
sqlite_file = 'db.sqlite3'  

# Nombre de la tabla que deseas exportar
table_name = 'users_userprofile'  # ← reemplaza con el nombre real de tu tabla

# Nombre del archivo Excel de salida
excel_file = f'{table_name}.xlsx'

# Conexión a la base de datos
conn = sqlite3.connect(sqlite_file)

# Leer los datos de la tabla a un DataFrame
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

# Escribir el DataFrame a un archivo Excel
df.to_excel(excel_file, index=False)

print(f"Exportación a Excel completa: {excel_file}")

# Cierra la conexión
conn.close()
