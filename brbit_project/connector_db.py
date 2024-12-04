import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Conexão com o banco de dados realizada com sucesso!")
    cursor = connection.cursor()
except Error as e:
    print(f"Erro ao conectar ao banco : {e}")
    connection = None
    cursor = None