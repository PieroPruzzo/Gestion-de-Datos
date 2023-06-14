import requests
import json
import mysql.connector as connector

url = "https://txirwghrsdfhlnt.form.io/proyecto/submission?limit=10"

response = requests.request("GET", url)

data = json.loads(response.text)

# Ordenamos el Json para que sea legible

dataj = json.dumps(data,indent=4)

#print(dataj)


for elemento in data: 
    try:
        connection = connector.connect(host='localhost',
                                       #El nombre de la base de datos se debe cambiar al del entregable final que se va a llamar "entrega3"
                                        database='entrega2',
                                        user='root',
                                        password='')
        
        mySql_insert_query = f"""INSERT INTO proyecto (nombre,direccion) 
        VALUES (
        '{elemento['data']['nombre']}',
        '{elemento['data']['direccion']}') """

        print(mySql_insert_query)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()

    except connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")