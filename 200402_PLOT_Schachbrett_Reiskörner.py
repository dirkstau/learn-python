"""
Reiskornlegende graphisch mit matplotlib.

Dieses Script berechnet die berühmte Reiskornlegende von Sissa ibn Dahir
und zeigt das Ergebnis anhand eines Graphen unter Nutzung der
matplotlib.
"""

import matplotlib.pyplot as plt
summe = 0
feldListe = []

for feld in range(64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1:>2}: {reiskorn:>25,} Reiskörner und damit insgesamt \
          {summe:>26,} Reiskörner")

gewicht = summe * 0.02 / 1000000
print(f"Das Gesamtgewicht beträgt etwa {gewicht:,.0f} t")

plt.plot(feldListe)
plt.show()
