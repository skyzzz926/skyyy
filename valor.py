import os
os.system ("cls")

i = 0
notas = 0

while true:
    nota = int(input("digite uma nota"))

    if nota < 0:
        break
    notas += nota
    i += 1

    resultado =notas/i
    print(resultado)
    
