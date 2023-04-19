#!/usr/bin/python3

import random

print("""
Milyen műveletet szeretne gyakorolni?

    1. Összeadás
    2. Kivonás
    3. Szorzás

""")

valasz = int(input("Választás (1-3): "))
print("")

ok = 0
db = 0
while ok < 5:
    db = db + 1
    a = random.randint(1,10)
    b = random.randint(1,10)
    if valasz == 1:
	    c = int(input("{0}+{1} = ".format(a, b)))
	    d = a+b
    elif valasz == 2:
	    c = int(input("{0}-{1} = ".format(a, b)))
	    d = a-b
    else:
	    c = int(input("{0}*{1} = ".format(a, b)))
	    d = a*b
    if c == d:
	    ok = ok + 1
	    print("Helyes!")
    else:
	    print("Hibás!")
print("\nGratulálunk!\nSikerült 5 helyes műveletet elvégezni {0} próbálkozásból.\n".format(db))

