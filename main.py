# användarinput
namn = input("Ange ditt namn: ")
print (namn)

# input ger sträng, måste konvertera sträng till annan datatyp, float/int etc innan
# vanligaste misstaget, inte konverterar datatyp KOM IHÅG
tal_1 = float(input("Ange tal 1: "))
tal_2 = float(input("Ange tal 2: "))
total = tal_1 * tal_2
print(total)

# nytt exempel

nyttExempelNamn = input("Ange ditt namn: ") # blir string

exempelTal1 = float(input("Ange första talet: "))

exempelTal2 = float(input("Ange andra talet: "))

exempeltotal = exempelTal1 / exempelTal2

print(exempeltotal)

# test fortsätt sen



räknesätt = input("Ange räknesätt: (*, /, +, -)")

# IF THEN ELSE

# om anna är längre än oskar, gör följande : ___
# om ett viss vilkor är uppfyllt ska någonting hända
# >= större än lr likamed.
# <= mindre än lr likamed.
# > större än
# < mindre än
# == -> jämförelseoperator



anna = 12
oskar = 12

if anna != oskar:
        print("true")
else :
        print("false")
# jämförelseoperatorer
# ==, >, <, <=, >=, !=
# == är de lika med varandra
# != är de inte lika med varandra

# undvik not,
# not finns inte i andra programeringsspråk ANVÄND !=
if not anna == oskar:
    print("true")
if anna > oskar:
        print("Stämmer")
else:
        print("Stämmer ej")

if anna > oskar:
    print("större")
elif anna == oskar:
        print("lika stora")

# ^^ funkar inte

