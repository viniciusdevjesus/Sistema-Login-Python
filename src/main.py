from Window import Email_name
from Window import Password_name
import mysql.connector
conect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='BD_CLI'
)
cursor = conect.cursor()
logName = str(input("Digite seu email: "))
logPassword = str(input("Digite sua senha: "))
comando = "SELECT '{}' FROM Clientes".format(logName)
cursor.execute(comando)
resultado = cursor.fetchall()


def Login():
    conect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='BD_CLI'
    )
    cursor = conect.cursor()
    comando1 = "SELECT '{}' FROM Clientes".format(Email_name)
    comando2 = "SELECT '{}' FROM Clientes".format(Password_name)
    cursor.execute(comando1)
    cursor.execute(comando2)
    resultado1 = cursor.fetchall()
    resultado2 = cursor.fetchall()
    if resultado == Email_name:
        print ("ok")



# print("========Sistema de Cadastro de Clientes=======")
# decision = int(input("[1] - Login\n[2] - Cadastro\n"))
# if decision == 1:
#     logName = str(input("Digite seu email: "))
#     logPassword = str(input("Digite sua senha: "))
#     comando = 'SELECT {logName} FROM Clientes'
#     cursor.execute(comando)
#     resultado = cursor.fetchall()
#     if resultado != logName:
#         print("Login incorreto")


# # comando = 'INSERT INTO(nome,numero,email,senha) VALUES ()'
# # cursor.execute(comando)
# # conect.commit() # edita o banco de dados 
# # resultado = cursor.fetchall() # ler o banco de dados

cursor.close()
conect.close()