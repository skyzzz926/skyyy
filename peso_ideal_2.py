import os
os.system ("clear")

altura = float(input("digite sua altura em metros"))
genero = str(input("""digite seu gênero:
m -masculino
f -feminino"""))
match gênero:

case "m":
   peso_ideal = (72.7 * altura) - 58
   print (f"0 peso ideal é: {peso_ideal:.2f}")


case "f":
   peso_ideal = (62.1 * altura) - 44.7
   print (f"0 peso ideal é: {peso_ideal:.2f}")

   case _: 
    print("opção invalida")