import mysql.connector

try:
    connection = mysql.connector.connect(
        host='',
        user='root',
        password='',
        database='sakila',
        ssl_disabled=True
    )

    if connection.is_connected():
        print('Conexión exitosa a la base de datos')
        cursor = connection.cursor()
        cursor.execute('SHOW TABLES')
        for table in cursor:
            print(table)

except mysql.connector.Error as e:
    print(f'Erroa al conectar MySQL: {e}')

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('Conexión cerrada')
