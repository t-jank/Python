print("Podaj wzrost w metrach")
wzrost = float(input())
waga = int(input("Podaj wagę\n"))
#wiek = int(input("podaj wiek\n"))
#S=-161
BMI = waga / (wzrost ** 2)
#zapotrz = (10*waga+6.25*100*wzrost-5*wiek+S)*1.6
#print("Twoje zapotrzeb kal wynosi:",zapotrz,"kcal.")
print("Twoje bmi wynosi: %.2f" % BMI)
if BMI < 18.5:
    print("Niedowaga")
elif 18.5 <= BMI <= 24:
    print("Waga normalna")
elif 24 < BMI <= 26.5:
    print("Lekka nadwaga")
elif BMI > 26.5:
    print("Nadwaga.", end=' ')
    if 30 <= BMI < 35:
        print("Otyłość I stopnia")
    elif 35 <= BMI < 40:
        print("Otyłość II stopnia")
    elif BMI >= 40:
        print("Otyłość III stopnia")
    else:
        print("Po prostu nadwaga.")
