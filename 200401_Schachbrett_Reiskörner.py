"""Dieses Script berechnet die berühmte Reiskornlegende von Sissa ibn Dahir."""

summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("Feld {:>2}: {:>25,} Reiskörner und damit insgesamt \
          {:>26,} Reiskörner".format(feld+1, reiskorn, summe))

gewicht = summe * 0.02 / 1000000
print("Das Gesamtgewicht beträgt etwa {:,.0f} t".format(gewicht))
