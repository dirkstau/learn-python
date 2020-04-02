"""Visualisierung der Zahl pi auf 1 Mio Nachkommastellen."""

with open("pi1000000.txt", "r") as f:
    pi = f.read()

print(len(pi))
