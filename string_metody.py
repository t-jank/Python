imie=input("Jak ci na imię? (: ")
nazwisko=input("Nazwisko! ;0 ")
tel=input("numer telefonu: ")
print("imie: ", imie.isalpha()) #czy tylko litery
print("nazwisko: ", nazwisko.isalpha())
print("numer telefonu: ", tel.isdigit()) # czy tylko cyfry
imie=imie.capitalize() # zmiana pierwszej litery na dużą
nazwisko=nazwisko.capitalize()
tel=tel.replace(" ", "")
tel=tel.replace("-", "")
print("czy_kobieta?: ", imie.endswith("a"))
personal = imie + " " + nazwisko + " " + tel
print(personal)
print(len(personal)) # liczba znaków w ciągu 'personal'
print(len(personal)-11) # liczba liter w napisie 'personal'
