from tkinter import *
import tkinter.ttk as ttk
from currency_program import *
    
def convert():
    """Function that convert one currency into another"""
    try:
        source_currency = Currency(cb_value1.get())
        target_currency = Currency(cb_value2.get())
        cb_value3.set((source_currency.converter(target_currency, float(amount.get())))) # writing the result
    except ValueError:
        cb_value3.set("The amount given must be a number!")
    except KeyError:
        cb_value3.set("No appropriate data!")

def sourceCurrency(event):
    """ 
    Command issued after selecting the source currency, 
    
    returns
    -------
    currency code
    """
    return(cb_value1.get())

def targetCurrency(event):
    """ 
    Command issued after selecting the target currency, 
    
    returns
    -------
    currency code
    """
    return(cb_value2.get())

# creating a window and setting a title and dimentions
root = Tk()
root.title("Currency converter")
root.geometry('400x200')

# creating two labels (for the source and target currency)
Label(root, text="source currency").grid(row=0, column=0, padx=2)
Label(root, text="target currency").grid(row=0, column=1, padx=2)

# creating two comboboxes (for the source and target currency)
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

# creating a label
Label(root, text="Enter the amount in the source currency:").grid(row=2, column=0,  padx=2, pady=6)

# creating a space to write an amount
amount = Entry(root)
amount.grid(row=2, column=1)

# creatind a label
result_label = Label(root, text="Amount in a target currency:")
result_label.grid(row=3, column=0, padx=2)

# creating a space, where the result will appear
cb_value3 = StringVar()
result = Label(root, textvariable = cb_value3)
result.grid(row=3, column=1)

# creating two bottons
btn1 = Button(root, text="Convert", command=convert)
btn2 = Button(root, text="Close", command=quit)
btn1.place(x=155, y=110)
btn2.place(x=155, y=150)


root.mainloop()

