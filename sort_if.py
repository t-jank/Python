# -*- coding: utf-8 -*-
a, b, c = 7, 13, 2
if a > b and a > c:
    print(a, end=", ")
    if b > c:
        print(b, ",", c)
    else:
        print(c, ",", b)
elif b > a and b > c:
    print(b, end=", ")
    if a > c:
        print(a, ",", c)
    else:
        print(c, ",", a)
else:
    print(c, end=", ")
    if a > b:
        print(a, ",", b)
    else:
        print(b, ",", a)
