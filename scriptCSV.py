import sqlite3
import csv

# Ruta al archivo SQLite
sqlite_file = 'db.sqlite3'

# Nombre de la tabla que deseas exportar (modifica esto según tu necesidad)
table_name = 'smartpots_smartpot'  # ← reemplaza con el nombre real de tu tabla

# Nombre del archivo CSV de salida
csv_file = f'{table_name}.csv'

# Conexión a la base de datos
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()

# Ejecuta una consulta para obtener los datos de la tabla
cursor.execute(f"SELECT * FROM {table_name}")
rows = cursor.fetchall()

# Obtiene los nombres de las columnas
column_names = [description[0] for description in cursor.description]

# Escribe los datos en un archivo CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(column_names)  # Escribe encabezados
    writer.writerows(rows)         # Escribe filas

print(f"Exportación completa: {csv_file}")

# Cierra la conexión
conn.close()
