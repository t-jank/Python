# -*- coding: utf-8 -*-
names = {"Szymon": "męskie",
         "Aleksander": "męskie",
         "Piotr": "męskie",
         "Maciej": "męskie",
         "Tomasz": "męskie",
         "Kinga": "żeńskie",
         "Aleksandra": "żeńskie",
         "Monika": "żeńskie",
         "Kuba": "męskie",
         "Kamil": "męskie",
         "Emilia": "żeńskie",
         "Karolina": "żeńskie",
         "Wojciech": "męskie",
         "Łukasz": "męskie",
         "Przemo": "męskie",
         "Olo": "męskie",
         "Napoleon": "męskie",
         "Grzegorz": "męskie",
         "Jakub": "męskie",
         "Magnus": "męskie",
         "Tomo": "męskie",
         "Maja": "żeńskie",
         "Weronika": "żeńskie",
         "Roksana": "żeńskie",
         "Jan": "męskie",
         "Mateusz": "męskie",
         "Mieszko": "męskie"}
new = input("Podaj imię: ")
new = new.title()
if(new in names.keys()):
    print(new, "to imię", names[new])
else:
    sex = input("Nie znamy tego imienia. Jest ono męskie czy żeńskie?: ")
    names[new] = sex
    print(names)
