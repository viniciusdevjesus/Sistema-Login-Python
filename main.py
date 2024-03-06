import mysql.connector
conect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12162007Vv',
    database='bdcli'
)
cursor = conect.cursor()
print("========Sistema de Cadastro de Clientes=======")
decision = int(input("[1] - Login\n[2] - Cadastro\n"))
if decision == 1:
    logName = str(input("Digite seu email: "))
    logPassword = str(input("Digite sua senha: "))
    comando = 'SELECT {LogName} FROM Cliente'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    if resultado != logName:
        print("Login incorreto")


# comando = 'INSERT INTO(nome,numero,email,senha) VALUES ()'
# cursor.execute(comando)
# conect.commit() # edita o banco de dados 
# resultado = cursor.fetchall() # ler o banco de dados

cursor.close()
conect.close()