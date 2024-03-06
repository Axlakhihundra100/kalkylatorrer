# importerar matte för om jag ville använda pi senare
import math


# definierar att add(x, y) plussar x och y
def add(x, y):
    return x + y


# definierar att sub(x, y) minusar x och y
def sub(x, y):
    return x - y


# definierar att div(x, y) dividerar x med y OCH ifall nämnaren är 0 blir svaret att miniräknaren inte kan dela med noll
def div(x, y):
    if y == 0:
        return "kan inte dela med noll"
    return x / y


# definierar att mult(x , y) multiplicerar x och y
def mult(x, y):
    return x * y


# instruktioner för användaren.
while True:
    print("_______________________________________________")
    print("| Inställningar:                              |")
    print("| Skriv add för addition                      |")
    print("| Skriv sub för subtraktion                   |")
    print("| Skriv mult för multiplikation               |")
    print("| Skriv div för division                      |")
    print("| Skriv avsluta för att stänga av programmet  |")
    print("_______________________________________________")
    # anger att det är här användaren skriver
    user_input = input(": ")
    # om användaren skriver avsluta avslutar programmet, break betyder avsluta.
    if user_input == "avsluta":
        break
    # anger att user input kan vara add sub o mult o div
    # användarinput float, för första o andra nummr
    elif user_input in ("add", "sub", "mult", "div",):
        x = float(input("Skriv ditt första nummer: "))
        y = float(input("Skriv ditt andra nummer: "))
        if user_input == "add":  # funktionsanrop ifall usrinput är add
            resultat = add(x,
                           y)  # adderar samma princip för resten, säger också att resultatet är funktionen add(x, y) x +y
        elif user_input == "sub":
            resultat = sub(x, y)
        elif user_input == "mult":
            resultat = mult(x, y)
        elif user_input == "div":
            resultat = div(x, y)
        elif user_input == "avsluta":
            break
    print("Resultat:", resultat)
