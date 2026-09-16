import random
print("1 - papier")
print("2- kamień")
print("3- nożyczki")

gracz = int(input("Wybierz kontre: "))
if gracz > 3:
    print("Error 404")
else:
     randomowa = random.randint(1,3)
if gracz == 1:
    if randomowa == 2:
        print("Wygrałeś")
    elif randomowa == 1:
        print("remis")
    elif randomowa == 3:
       print("przegrałes") 
if gracz == 2:
    if randomowa == 1:
        print("przegrałes")
    elif randomowa == 3:
        print("wygrales")
    elif randomowa == 2:
        print("remis")
if gracz == 3:
    if randomowa == 1:
        print("wygrales")
    elif randomowa == 2:
        print("przegrałes")
    elif randomowa == 3:
        print("remis")
        
print("Bot wybrał: ",randomowa)
