# simpel miniräknare
väljräkning = input("hur villdu räkna? (fyraräknesätten, cirkelnsomkrets)")
if väljräkning == "fyraräknesätten":
    tal1 = float(input("Ange tal ett: "))
    tal2 = float(input("Ange tal två: "))

    räknesätt = input("Ange räknesätt (*, /, +, -): ")

    if räknesätt == "*":
        multiplikation = tal1 * tal2
        print(multiplikation)
    elif räknesätt == "/":
        division = tal1 / tal2
        print(division)
    elif räknesätt == "+":
        plus = tal1 + tal2
        print(plus)
    elif räknesätt == "-":
        minus = tal1 - tal2
        print(minus)
elif väljräkning == "cirkelnsomkrets":
    π = 3.14159265359
    tall1 = float(input("Ange radien av din cirkel: "))
    svar = tall1 *2 * π
    print(svar)


