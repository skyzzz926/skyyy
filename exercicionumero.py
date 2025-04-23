import os

QUANTIDADE_NUMEROS = 6
lista_numeros = []
pares = 0
impares = 0

print ("lista de numeros")
for i in range (QUANTIDADE_NUMEROS):
    NUMERO = int(input("digite um numero: "))
    lista_numeros.append(NUMERO)

    if NUMERO % 2 == 0:
        pares += 1
    else:
        impares += 1

    print("\n= ITENS DA LISTA =")

for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}: {numero}")

print(f"\pares: {pares}")


print(f"\impares: {impares}")

