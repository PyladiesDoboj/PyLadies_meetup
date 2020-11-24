#Izračunati zbir unetih brojeva. Brojeve unositi dok se ne unese 0.

x = int(input("Unesi broj: "))
s = 0
while x != 0:
        s = s + x
        x = int(input("Unesi broj: "))
print("Zbir unetih brojeva je ", s)
