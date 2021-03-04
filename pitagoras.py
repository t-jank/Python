# -*- utf-8 -*-
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a > b and a > c:
    temp = c
    c = a
    a = temp
elif b > a and b > c:
    temp = c
    c = b
    b = temp
if a + b <= c:
    print("Nie da się zbudować trójkąta")
elif a**2 + b**2 == c**2:
    print("Trójkąt prostokątny")
    if a/3 == b/4 == c/5 or a/4 == b/3 == c/5:
        print("Trójkąt pitagorejski egipski")
else:
    print("Trójkąt, po prostu trójkąt.")
