import os 

os.system("clear")


numero1 = int(input(" digite um numero: "))

numero2 = int(input(" digite um numero: "))

operador =input(" digite a operação que deseja ( / - + * )")

match operador:
  
   case "+":

   resultado = numero1 + numero2

    case "-":

   resultado = numero1 + numero2

    case "/":

   resultado = numero1 + numero2

    case "*":

   resultado = numero1 + numero2

   case _:
       resultado = "operação invalida"
       