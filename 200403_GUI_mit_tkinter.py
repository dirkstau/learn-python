from tkinter import *

fenster = Tk() #Erzeugung eines Fensters
fenster.title("Mein GUI-Programm")
fenster.geometry("500x500")

def ausgabe(): #Funktion zur Ausgabe eines Strings in der Konsole
    print("Hello World!")

def sqrt()

knopf1 = Button(fenster, text="Klick mich!", command = ausgabe) #Erzeugung einer Schaltfläche
knopf1.pack()

eingabe = Entry(fenster)
eingabe.pack()

label1 = Label()
label1.pack()

def rechnen(): #Funktion zum Rechnen
    label1.configure(text=eingabe.get())


knopf2 = Button(fenster, text="Ich lese",command=lesen)
knopf2.pack()

mainloop()
