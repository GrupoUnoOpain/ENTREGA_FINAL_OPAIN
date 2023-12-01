import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('opainapp.db')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Consultar los datos
cursor.execute('SELECT * FROM user')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
