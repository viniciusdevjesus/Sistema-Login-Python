# from Window import Email_name
# from Window import Password_name
import mysql.connector
conect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='BD_CLI'
)
cursor = conect.cursor(buffered=True)
logName = str(input("Digite seu email: "))
logPassword = str(input("Digite sua senha: "))

# comando = "SELECT '{}' FROM Clientes".format(logName)
# cursor.execute(comando)
# resultado = cursor.fetchall()


def Login():
    comando1 = "SELECT * FROM Clientes WHERE nome= '{}'".format(logName)
    comando2 = "SELECT * FROM Clientes WHERE senha= '{}'".format(logPassword)
    cursor.execute(comando1)
    resultado1 = cursor.fetchall()
    cursor.execute(comando2)
    resultado2 = cursor.fetchall()
    for row in resultado1:
        if logName in row:
            print("acertou o email")
        else:
            print("Eroou o email")
    for row in resultado2:
        if logPassword in row:
            print("acertou a senha")
        else:
            print("Eroou a senha")


print(Login())
# # comando = 'INSERT INTO(nome,numero,email,senha) VALUES ()'
# # cursor.execute(comando)
# # conect.commit() # edita o banco de dados 
# # resultado = cursor.fetchall() # ler o banco de dados

cursor.close()
conect.close()