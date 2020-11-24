"""
Napisati program kojim se za dati jedinstveni matični broj građanina određuju
dan, mesec i godinu rođenja i ispisuju u formatu DD.MM.GGGG.
(Smatrati da je taj građanin rođen u periodu od 1100. do 2020. godine.)
"""

jmbg = input("Unesite Vaš jmbg:")
if len(jmbg) == 13:
        dan = jmbg[0:2]
        mesec = jmbg[2:4]
        god = jmbg[4:7]
        if jmbg[4] == "0":
                godina = "2" + god
        else:
                godina = "1" + god
        print(dan + "." + mesec + "." + godina + ".")
	
else:
        print("Pogrešan unos.")
