"""Dieses Script berechnet die berühmte Reiskornlegende von Sissa ibn Dahir."""

summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe += reiskorn
    print(f"Feld {feld+1:>2}: {reiskorn:>25,} Reiskörner und damit insgesamt \
          {summe:>26,} Reiskörner")

gewicht = summe * 0.02 / 1000000
print(f"Das Gesamtgewicht beträgt etwa {gewicht:,.0f} t")
