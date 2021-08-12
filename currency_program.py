import requests
from bs4 import BeautifulSoup
    
def dictionary(url):
    """
    Funkcja zwraca słownik postaci {kod_waluty:[nazwa_waluty, kurs_średni]},
    za argument przyjmuje zawartość pliku typu xml pobranego ze strony nbp
    """
    soup = BeautifulSoup(url, "lxml")
    names = soup("currency")
    codes = soup("code")
    rates = soup("mid")
    
    names_list = ["złoty (Polska)"]
    for name in names:
        names_list.append(name.get_text())

    codes_list = ["PLN"]
    for code in codes:
        codes_list.append(code.get_text())

    rates_list = [1.0]
    for rate in rates:
        rates_list.append(float(rate.get_text()))

    dictionary ={}
    for i in range(len(names_list)):
        dictionary[codes_list[i]] = [names_list[i], rates_list[i]]

    return dictionary

#gdy wystąpi błąd przy pobieraniu aktualnych kursów walut (np. brak dostępu do internetu),
#program użyje danych z ostatnio pobranej tabeli
#jeśli nie nastąpi błąd program pobierze dane bezpośrednio ze strony nbp i nadpisze plik xml
try:
    r = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/?format=xml")
    d = dictionary(r.text)
    with open("kursy_walut.xml", "wb") as f:
        f.write(r.content)
except:
    with open("kursy_walut.xml") as f:
        d = dictionary(f.read())

class Currency:

    def __init__(self, c):
        """
        Tworzy wlutę o konkretnym kodzie, nazwie i kursie średnim,
        wykorzystuje do tego wcześniej utworzony słownik,
        za argumnet przyjmuje kod waluty
        """
        self.c = c
        self.n = d[self.c][0]
        self.r = d[self.c][1]

    def converter(self, currency, x):
        """
        Funkcja przelicza podaną kwotę (arument x)
        z waluty źródłowej, na docelową (argument currency)
        """
        if type(x) == int or type(x) == float:
            return round((self.r/currency.r) * x, 2)
        else:
            raise("Podana wartość musi być liczbą!")
