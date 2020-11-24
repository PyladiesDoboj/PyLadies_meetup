"""
      KVIZ
"""
print('Kviz znanja iz programskog jezika Python')
broj_tacnih = 0
# Pitanje 1
print('1. Za pisanje komentara u jednoj liniji koristi se znak:', end=' ')
odgovor = input()
if odgovor=='#':
    print('Tačno!')
    broj_tacnih+=1
else:
    print('Pogrešno. Tačan odgovor je #.')

#Pitanje 2
print('2. Koju vrednost ima izraz 23//2', end=' ')
odgovor = input()
if odgovor=='11':
    print('Tačno!')
    broj_tacnih+=1
else:
    print('Pogrešno. Tačan odgovor je 11.')
    
print('Broj tačnih odgovora je:', broj_tacnih)


