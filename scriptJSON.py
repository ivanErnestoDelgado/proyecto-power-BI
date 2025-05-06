import sqlite3
import json

# Ruta al archivo SQLite
sqlite_file = 'db.sqlite3'

# Nombre de la tabla que deseas exportar
table_name = 'smartpots_alert'  # ← reemplaza esto con el nombre real de tu tabla

# Nombre del archivo JSON de salida
json_file = f'{table_name}.json'

# Conexión a la base de datos
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()

# Ejecutar consulta para obtener los datos
cursor.execute(f"SELECT * FROM {table_name}")
rows = cursor.fetchall()

# Obtener los nombres de las columnas
columns = [description[0] for description in cursor.description]

# Convertir los datos a una lista de diccionarios
data = [dict(zip(columns, row)) for row in rows]

# Guardar en archivo JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Exportación completa: {json_file}")

# Cerrar conexión
conn.close()
