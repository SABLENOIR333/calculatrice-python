def addition(a, b):
    return a + b
def multiplication(a, b):
    return a * b
def divisition(a, b):
    return a // b
def soustraction(a, b):
    return a - b 
def parametre(choix, a , b):
    if choix == "+" or choix == "addition" or choix == "add":
        return addition(a,b)
    elif choix == "-"  or choix == "soustraction" or choix == "sub":
        return soustraction(a,b)
    elif choix == "/" or choix == ":" or choix == "div"  or choix == "division" or choix == "//":
        return divisition(a,b)
    elif choix == "*" or choix == "multiplication" or choix == "mult" or choix.lower() == "x":
        return multiplication(a,b)
    else :
        return "valeur inconnue"
def question():
    ask = input("voulez vous calculer ? (oui/non)")
    ask = ask.lower()
    while ask != "oui" and ask != "non":
        ask = input("voulez vous calculer ? (oui/non)")
        ask = ask.lower()
    return ask


while question() == "oui":
    a = int(input("donne un nombre"))
    b = int(input("donne un nombre"))
    choix = input("fais un choix")
    if b == 0 or a == 0 and choix == "/":
        print("erreur division par 0")  
        continue
    print(parametre(choix, a , b))
    if question() == "non":
        print("merci d'avoir utilisé notre calculatrice")
        break
print("fin du programme")