"""
Napisati funkciju koja datu listu sortira u rastućem poretku.
U glavnom delu programa uneti listu od n celih brojeva a zatim korišćenjem napis
ane funkcije sortirati elemente liste.
"""
def sortiranje(lista):
    lista.sort()
A=[]
n=int(input("Koliko brojeva želite da sortirate"))
print ("Unesite željene brojeve. Nakon svakog unosa pritisnite Enter")
for i in range(n):
    A.insert(i,int(input()))
print(A)
sortiranje(A)
print(A)
