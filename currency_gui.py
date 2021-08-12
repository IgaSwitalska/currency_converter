from tkinter import *
import tkinter.ttk as ttk
from waluta_program import *
    
def convert():
    """
    Funkcja przelicza kwotę podaną przez użytkownika
    z waluty źródłowej na docelową
    (również wybranych przez użytkownka)
    """
    try:
        w1 = Currency(cb_value1.get()) #waluta źródłowa
        w2 = Currency(cb_value2.get()) #waluta docelowa
        cb_value3.set((w1.converter(w2, float(amount.get())))) #wypisanie wyniku
    except ValueError:
        cb_value3.set("Podana wartość musi być liczbą!")
    except KeyError:
        cb_value3.set("Brak odpowiednich danych!")

def sourceCurrency(event):
    """Komenda wywołana po wybraniu waluty źródłowej, zwraca kod waluty"""
    return(cb_value1.get())

def targetCurrency(event):
    """Komenda wywołana po wybraniu waluty docelowej, zwraca kod kaluty"""
    return(cb_value2.get())

#stworzenie okienka, o określonym tytule i wymiarach
root = Tk()
root.title("Przelicznik walut")
root.geometry('400x200')

#stworzenie dwóch etykiet (dla waluty źródłowej i docelowej)
currency1_label = Label(root, text="waluta źródłowa")
currency1_label.grid(row=0, column=0, padx=2)

currency2_label = Label(root, text="waluta docelowa")
currency2_label.grid(row=0, column=1, padx=2)

#stworzenie dwóch list rozwijanych (dla waluty źródłowej i docelowej)
cb_value1 = StringVar()
combobox1 = ttk.Combobox(root, textvariable = cb_value1)
combobox1.grid(row=1, column=0, padx=2)
combobox1['values'] = (list(d.keys()))

combobox1.bind("<<ComboboxSelected>>", sourceCurrency)

cb_value2 = StringVar()
combobox2 = ttk.Combobox(root, textvariable = cb_value2)
combobox2.grid(row=1, column=1)
combobox2['values'] = (list(d.keys()))

combobox2.bind("<<ComboboxSelected>>", targetCurrency)

#stworzeine etykiety
label = Label(root, text="Podaj kwotę w walucie źródłowej:")
label.grid(row=2, column=0,  padx=2, pady=6)

#storzenie pola do wpisania kwoty w walucie źródłowej
amount = Entry(root)
amount.grid(row=2, column=1)

#stworzeine etykiety
result_label = Label(root, text="Kwota w walucie docelowej:")
result_label.grid(row=3, column=0, padx=2)

#storzenie pola, gdzie będzie się wyświetlać wynik
cb_value3 = StringVar()
result = Label(root, textvariable = cb_value3)
result.grid(row=3, column=1)

#stworzenie dwóch przycisków (uruchamiający obliczenia i kończący program)
btn1 = Button(root, text="Przelicz", command=convert)
btn2 = Button(root, text="Koniec", command=quit)
btn1.place(x=155, y=110)
btn2.place(x=155, y=150)


root.mainloop()

