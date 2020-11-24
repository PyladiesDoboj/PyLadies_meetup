"""
Napišite funkcije za sabiranje dva broja i pozovite je u glavnom delu programa.
Omogućite izvršavanje te funkcije 3 puta.
"""

def sabiranje():
    a = int(input("Unesite prvi broj: "))
    b = int(input("Unesite drugi broj: "))
    c = a + b
    print ("Zbir unetih brojeva je:", c)

for i in range(1,4):
    sabiranje()
    print ("-"*15)
