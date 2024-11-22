import mysql.connector
import pandas as pd

try:
    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host='',
        user='root',
        password='',
        database='sakila',
        ssl_disabled=True
    )

    if connection.is_connected():
        print('Conexión exitosa a la base de datos')

        # Crear un cursor y ejecutar una consulta
        query = 'SELECT * FROM actor'  # Ejemplo: seleccionar todos los datos de la tabla 'actor'
        cursor = connection.cursor()
        cursor.execute(query)

        # Convertir los resultados en un DataFrame de Pandas
        columns = [col[0] for col in cursor.description]  # Obtener nombres de las columnas
        results = cursor.fetchall()  # Obtener todos los registros
        df = pd.DataFrame(results, columns=columns)

        # Mostrar el DataFrame
        print(df.head())  # Mostrar las primeras filas del DataFrame

except mysql.connector.Error as e:
    print(f'Error al conectar MySQL: {e}')

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('Conexión cerrada')
