import mysql.connector

def ConnectToDatabase(db):
    connection = mysql.connector.connect(host=db['mysql_host'],database=db['mysql_db'],user=db['mysql_user'],password=db['mysql_password'])
    cursor = connection.cursor()

    return connection,cursor