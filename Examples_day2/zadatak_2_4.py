#Napisati program koji uneti ceo broj n ispisuje sa ciframa u obrnutom poretku.

n = int(input("Unesi broj:"))
while n > 0:
    print(n % 10, end=' ')
    n = n // 10
