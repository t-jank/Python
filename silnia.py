# -*- coding: utf-8 -*-

# zad.4

# silnia na pętli for
f = 1
n = input("Podaj liczbę: ")
while n.isdigit() == False:
    n = input("Podaj liczbę całkowitą dodatnią: ")
n = int(n)
while n < 0:
    n = int(input("Podaj liczbę całkowitą dodatnią: "))
if n == 0 or n == 1:
    f = 1
else:
    for i in range(1, n+1):
        f = i * f
print("Silnia liczby %d jest równa %d." % (n, f))
"""
# silnia na pętli while
f, i = 1, 1
n = input("Podaj liczbę: ")
while n.isdigit() == False:
    n = input("Podaj liczbę całkowitą dodatnią: ")
n = int(n)
#while n < 0:
#    n = int(input("Podaj liczbę całkowitą dodatnią: "))
if n == 0 or n == 1:
    f = 1
else:
    while i < n + 1:
        f = i * f
        i += 1
print("Silnia liczby %d jest równa %r." % (n, f))
"""
