"""
Napišite funkciju pod nazivom pravougaonik koja prihvata dva cela broja m i n
kao argumente i štampa m × n boks koji se sastoji od zvezdica.
"""
def pravougaonik(m,n):
    for i in range(m):
        print('*' * n)

pravougaonik(3,7)
