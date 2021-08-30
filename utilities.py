import mysql.connector
import re

def CheckUsername(name):
    UsernamePattern = "^[a-zA-Z0-9_]+$"
    if not re.match(UsernamePattern, name):
        return True
    else:
        return False

def CheckPassword(password):
    PasswordPattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    PassCheck = re.compile(PasswordPattern)
    if not re.search(PassCheck, password):
        return True
    else:
        return False

def CheckEmail(email):
    EmailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(EmailPattern, email):
        return True
    else:
        return False


def ConnectToDatabase(db):
    connection = mysql.connector.connect(host=db['mysql_host'],database=db['mysql_db'],user=db['mysql_user'],password=db['mysql_password'],port=db['mysql_port'])
    cursor = connection.cursor()

    return connection,cursor