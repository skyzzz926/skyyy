import os

os.system ("cls")

for  i in range (3):
        login = input("digite login")
        senha = int(input("digite a sua senha"))
        if login != 'open' or senha != 2345:
           print("login ou senha incorreto!\n")

        else:
            print ("seja bem vindo")
            
        break