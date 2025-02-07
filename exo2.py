number1 = input("entrer un nombre entier ")
number2 = input("entrer un nombre entier ")

if not number1.isnumeric() or not number2.isnumeric() :
    print("erreur : ce ne sont pas des nombres")
    raise SystemExit("fin du programme")
else:
    number1 = int(number1)
    number2 = int(number2)

symbole_operation = input ("entrer le symbole de l'opération (+, -, * ou /) ")
symbole_operation_valide = ["+", "-", "*", "/"]

if(symbole_operation not in symbole_operation_valide) :
    print("L'opérateur n'est pas valide")
    raise SystemExit("fin de programme")
if symbole_operation == "/" and number2 == 0:
    raise SystemExit("Impossible de diviser par 0")

match symbole_operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        result = round(number1 / number2)
    case _:
        print("Impossible de réaliser l'opération")

print(result)

