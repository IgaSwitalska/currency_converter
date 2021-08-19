# Currency converter
A program that allows for the quick conversion of one currency into another currency.

The program was made as an university project. I have created this repository to see how can I change this program after a year of study.

## Instalation
To open the program you have to install this python libraries:
* requests,
* bs4,
* tkinter.

You can do it via pip, writing in the command line:

``` pip install requests ```

``` pip install requests bs4 ```

``` pip install requests tkinter ```

## About the aplication
You have to run the program from the **currency_gui.py** file.

Then you have to choose a source currency from the first drop-down list and a target currency from the second drop-down list (you can choose from 36 currencies).
Next press the botton **Przelicz**. The application will show a converted amount.

If occures any problem with download of actual currency rates (e.g. no internet connection), the program will use data from recently downloaded table.
If there's no problem, the program will download data directly from the website of National Bank of Poland and will overwrite xml file.
