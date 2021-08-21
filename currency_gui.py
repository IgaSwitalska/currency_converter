from tkinter import *
import tkinter.ttk as ttk
from currency_program import *
    
def convert():
    """Function that convert one currency into another"""
    try:
        source_currency = Currency(cb_value1.get().split(" ")[0])
        target_currency = Currency(cb_value2.get().split(" ")[0])
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

def rotation():
    source = cb_value1.get()
    target = cb_value2.get()

    cb_value1.set(target)
    cb_value2.set(source)

bg_color = "#8ebbde"
text_font = "Courier"

# creating a window and setting a title and dimentions
root = Tk()
root.title('Currency converter')
root.geometry('650x350')
root.configure(bg=bg_color)

Label(root,text='Currency converter', background=bg_color, font=(text_font,30)).place(x=90,y=10)

# creating two labels (for the source and target currency)
Label(root, text="source currency", background=bg_color, font=(text_font,15)).place(x=50,y=70)
Label(root, text="target currency", background=bg_color, font=(text_font,15)).place(x=400,y=70)

# creating two comboboxes (for the source and target currency)
cb_value1 = StringVar()
combobox1 = ttk.Combobox(root, textvariable = cb_value1, width=40)
combobox1.place(x=10,y=100)
combobox1['values'] = ["{} - {}".format(currency, d[currency][0]) for currency in  d.keys()]

combobox1.bind("<<ComboboxSelected>>", sourceCurrency)

cb_value2 = StringVar()
combobox2 = ttk.Combobox(root, textvariable = cb_value2, width=40)
combobox2.place(x=360,y=100)
combobox2['values'] = ["{} - {}".format(currency, d[currency][0]) for currency in  d.keys()]

combobox2.bind("<<ComboboxSelected>>", targetCurrency)

# creating a label
Label(root, text="Enter the amount in the source currency:", background=bg_color, font=(text_font,10)).place(x=10,y=130)

# creating a space to write an amount
amount = Entry(root)
amount.place(x=350,y=130)

# creatind a label
result_label = Label(root, text="Amount in a target currency:", background=bg_color, font=(text_font,10))
result_label.place(x=10,y=160)

# creating a space, where the result will appear
cb_value3 = StringVar()
result = Label(root, textvariable = cb_value3, background=bg_color, font=(text_font,10,"bold"))
result.place(x=280,y=160)

# creating two buttons
btn1 = Button(root, text="Convert", command=convert, bg="#cc7fe3", activebackground="#d4abe0", font=(text_font,10), height=2, width=15)
btn2 = Button(root, text="Close", command=quit, bg="#e3789e", activebackground="#db91ab", font=(text_font,10),height=2, width=8)
btn1.place(x=255, y=200)
btn2.place(x=280, y=260)

# rotate button
image = PhotoImage(file = "rotation_icon.png")
btn3 = Button(root, image=image, command=rotation)
btn3.place(x=300,y=80)


root.mainloop()
