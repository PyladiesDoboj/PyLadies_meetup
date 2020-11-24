"""
      KVIZ
"""
print('Kviz znanja iz programskog jezika Python')

pitanja = ['1. Za pisanje komentara u jednoj liniji koristi se znak: ',
           '2. Koju vrednost ima izraz 23//2 ']
odgovori = ['#','11']

broj_tacnih = 0
for i in range(len(pitanja)):
    odgovor = input(pitanja[i])
    if odgovor==odgovori[i]:
        print('Tačno')
        broj_tacnih=broj_tacnih+1
    else:
        print('Pogrešno.  Tačan odgovor je', odgovori[i])
        
print('Broj tačnih odgovora je:', broj_tacnih)



