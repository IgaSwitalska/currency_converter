import requests
from bs4 import BeautifulSoup
    
def dictionary(url):
    """
    Function that takes data from xml file and makes a dictionary

    args:
    -----
    url - a content of a xml file: exchange_rates.xml (string)

    returns
    -------
    dictionary: {currency_code:[currency_name, currency_rate]}
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


# download of actual currency rates
try:
    r = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/?format=xml")
    d = dictionary(r.text)
    with open("exchange_rates.xml", "wb") as f:
        f.write(r.content)
except:
    with open("exchange_rates.xml") as f:
        d = dictionary(f.read())

class Currency:

    def __init__(self, code):
        """
        Initializes a currency with with a specific code, name and rate.
        Uses a dictionary created before.

        args:
        -----
        code - currency code
        """
        self.code = code
        self.name = d[self.code][0]
        self.rate = d[self.code][1]

    def converter(self, currency, amount):
        """
        Funcion that convert an amount 
        from a source currency into a target currency.

        args:
        -----
        currency - target currency (an object from the class Currency)
        amount - the amount we want to convert (float)
        """
        if type(amount) == int or type(amount) == float:
            return round((self.rate/currency.rate) * amount, 2)
        else:
            raise("The amount given must be a number!")
