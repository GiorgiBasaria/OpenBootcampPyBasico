import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('alumnos.db')

# Creación de la tabla Alumnos
conn.execute('''CREATE TABLE Alumnos
             (id INTEGER PRIMARY KEY,
             nombre TEXT NOT NULL,
             apellido TEXT NOT NULL);''')

# Inserción de datos
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Juan', 'Pérez')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('María', 'González')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Pedro', 'García')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Laura', 'López')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Ana', 'Ruiz')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Carlos', 'Fernández')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Sara', 'Martínez')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('David', 'Sánchez')")

# Guardar los cambios en la base de datos
conn.commit()

# Búsqueda de un alumno por nombre
nombre_buscado = 'Juan'
alumno = conn.execute(f"SELECT * FROM Alumnos WHERE nombre = '{nombre_buscado}'").fetchone()
if alumno:
    print(f"Alumno encontrado: {alumno[1]} {alumno[2]}")
else:
    print("No se encontró ningún alumno con ese nombre.")

# Cerrar la conexión a la base de datos
conn.close()


