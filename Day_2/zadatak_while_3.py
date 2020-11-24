"""
Napiši program koji unosi imena studenata sve dok se ne unese prazan string
i na kraju prijavljuje koliko imena je uneto.
"""

broj = 0    
while input("Unesite ime: ") != "":
    broj =  broj+1  
print("Broj prijavljenih:", broj)
