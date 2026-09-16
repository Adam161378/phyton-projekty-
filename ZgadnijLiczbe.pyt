import random
print("Zgadnij liczbe od 1 do 10: ");
randomowa = random.randint(1, 10)
cyfra = int(input("Podaj cyfre: "))
while cyfra != randomowa:
    cyfra = int(input("Podaj cyfre: "))

    if cyfra > randomowa:
        print("Za duża cyfra")
    elif cyfra < randomowa:
        print("Za mała cyfra")
    else: 
        print ("Congratulations")