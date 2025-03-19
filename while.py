import os
os.system ("cls")

contador=0
continua= 's'

while continua== 's':
#comandos a serem repetidos
    print ("repetindo..............")
contador +=1
continua= input ("tecle 's desejo.").strip().lower()

if contador ==0:
    input("0 bloco NÃO foi repetido")
else: 
    print(f"o bloco foi repetido{contador}vezes")