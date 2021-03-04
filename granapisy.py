# -*- coding: utf-8 -*-
from random import randint
words = ["jabłko", "gruszka", "banan", "kiwi", "mango", "ogień",
         "prokrastynacja", "toast", "kasyno", "siłownia", "biblioteka",
         "restauracja", "kosmos", "łóżko", "szachownica", "programowanie",
         "termometr", "siatkówka", "żyrafa", "pingwin", "papuga", "słoń",
         "wielbłąd", "słońce", "długopis", "żółw", "ślimak", "książka", "pióro",
         "fryzjer", "basen", "gospodarka", "rower", "squash", "mandat", "kubek",
         "skakanka", "koronawirus", "politechnika", "morsowanie", "studia",
         "bumerang", "python", "list", "koperta", "niebieski", "różowy", "piwo"]
pswd = words[randint(0,len(words)-1)]

tmp = ["tmp"]
puzzle = ""
del tmp[0]
for i in range(len(pswd)):
    tmp.append(pswd[i])
#print(tmp)
i=0
tmp2 = ["tmp"]
del tmp2[0]
while tmp:
    n = randint(0,len(tmp)-1)
    tmp2.append(tmp[n])
    del tmp[n]
    i += 1
#print(tmp2)
for i in range(len(tmp2)):
    puzzle = puzzle + tmp2[i]
print(puzzle)
guessed = input("Zgadnij jakie to słowo: ")
while guessed != pswd:
    if guessed == "q" or guessed =="Q":
        print("Koniec. Poprawna odpowiedź:", pswd)
        break
    guessed = input("Źle. Spróbuj ponownie: ")
if guessed != "q" and guessed != "Q":
    print("Bardzo dobrze, gratulacje :)")
