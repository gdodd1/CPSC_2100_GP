from tkinter import *
from PIL import Image, ImageTk
import requests
import pickle

def main():
    
    exchangeRateDict = None #this dictionary is populated in the main
                            #program where the "scrape" function is called
    
    infile = open("code/currencies.dat",'rb') 
    countryDict = pickle.load(infile)  
    infile.close() 
    countries = [k for k in countryDict.keys() ]
    countries.sort()
    
    #converts the amount in amtA to the amount in  according to the selected country using in the exchange rate from the data from the scrape() function to amtB
    def convert():
        amount = float(amtA.get())
        from_country = countries[countryFrom.curselection()[0]]
        to_country = countries[countryTo.curselection()[0]]
        
        if from_country == to_country:
            amtB.set(str(amount))
            return
        
        # exchange rate dict is formatted as follows: {code: countryCode, rate: exchangeRate}

        toIndex = countries.index(to_country)
        fromIndex = countries.index(from_country)

        to_rate = exchangeRates[toIndex]
        from_rate = exchangeRates[fromIndex]
        
        converted_amount = amount / from_rate * to_rate
        amtB.set(str(round(converted_amount, 2)))

    
    def changeCountryFrom(event):
        cntry = countryDict[countries[countryFrom.curselection()[0]]][1]
        imgFrom = "images/" + cntry + ".jpg"
        imgCntryFrom = Image.open(imgFrom)
        cntryFrom = ImageTk.PhotoImage(imgCntryFrom)
        cntryFromLabel.configure(image = cntryFrom)
        cntryFromLabel.image=cntryFrom
        
        #this code is for when you put the flags in;
        # commented out for now

        #country = countries[countryFrom.curselection()[0]]
        #flagFrom = country + ".jpg"
        #imgFF = Image.open(flagFrom)
        #imgFlagFrom = ImageTk.PhotoImage(imgFF)
        #flagFromLabel.configure(image = imgFlagFrom)
        #flagFromLabel.image = imgFlagFrom
        
        if amtA.get() != '':
            convert()

    def changeCountryTo(event):
        cntry = countryDict[countries[countryTo.curselection()[0]]][1]
        imgTo = "images/" + cntry + ".jpg"
        imgCntryTo = Image.open(imgTo)
        cntryTo = ImageTk.PhotoImage(imgCntryTo)
        cntryToLabel.configure(image = cntryTo)
        cntryToLabel.image=cntryTo
        convert()

        country = countries[countryTo.curselection()[0]]
        flagTo = "images/" + country + ".jpg"
        imgTF = Image.open(flagTo)
        imgFlagTo = ImageTk.PhotoImage(imgTF) 
        flagToLabel.configure(image = imgFlagTo)
        flagToLabel.image = imgFlagTo 

        

    def addDigit(n):
        #function triggered whenever one of the number buttons is clicked
        
        #you will need to add functions for when the '.' and 'C' buttons are clicked
        oldval = amtA.get()
        amtA.set(oldval + n)
        convert()
    
    def decimal():
        if '.' not in amtA.get():
            amtA.set(amtA.get() + '.')
            convert()
        else:
            pass

    def clear():
        amtA.set('')
        amtB.set('')

    def scrapeCurrencies():
        url = 'https://api.currencyapi.com/v3/latest?apikey=P19VLkaXHT7BbkgKCppQBbcOgDCcLvBkRBUkW6Cl'
        response = requests.get(url)
        return response.json()       
            
    window = Tk()
    window.geometry("485x400")
    window.title("Currency Converter")
    
    imgArrow = Image.open("images/arrow.jpg")
    arrow = ImageTk.PhotoImage(imgArrow) 

    imgFrom = "images/" + countryDict[countries[0]][1].lower() + ".jpg"
    imgCntryFrom = Image.open(imgFrom)
    cntryFrom = ImageTk.PhotoImage(imgCntryFrom) 
    
    imgTo = "images/" + countryDict[countries[0]][1].lower() + ".jpg"
    imgCntryTo = Image.open(imgTo) 
    cntryTo = ImageTk.PhotoImage(imgCntryTo)
        
    title = Label(window,text="Currency Converter",font=('Calibri 18'),bg="blue",fg="yellow")
    title.grid(row=0, column=0, columnspan=7,sticky=NSEW)
    
    cntryFromLabel = Label(window,image=cntryFrom,width=55,height=40,bg="white") 
    cntryFromLabel.grid(row=1,column=0,sticky=E)
    
    cntryToLabel = Label(window,image=cntryTo,width=55,height=40,bg="white") 
    cntryToLabel.grid(row=1,column=0,sticky=W)

    flagToLabel = Label(window,image=cntryTo,width=55,height=40,bg="white")

    yscroll1 = Scrollbar(window,orient=VERTICAL)
    yscroll1.grid(row=1,column=1,sticky=NSEW)
    conOfCountryFrom = StringVar()
    countryFrom = Listbox(window,exportselection=0,listvariable=conOfCountryFrom,yscrollcommand=yscroll1.set)    
    countryFrom.grid(row=1,column=2,sticky=EW)
    conOfCountryFrom.set(tuple(countries))
    countryFrom.bind("<<ListboxSelect>>", changeCountryFrom)
    yscroll1["command"] = countryFrom.yview
    
    arrowLabel = Label(window,image=arrow) 
    arrowLabel.grid(row=1,column=3)
    
    yscroll2 = Scrollbar(window,orient=VERTICAL)
    yscroll2.grid(row=1,column=4,sticky=NSEW)
    conOfCountryTo = StringVar()
    countryTo = Listbox(window,exportselection=0,listvariable=conOfCountryTo,yscrollcommand=yscroll2.set)
    countryTo.grid(row=1,column=5,sticky=EW)
    conOfCountryTo.set(tuple(countries))
    countryTo.bind("<<ListboxSelect>>", changeCountryTo)
    yscroll2["command"] = countryTo.yview
    
    
    
    # make a new frame
    buttonFrame = Frame(window)
    buttonFrame.grid(row=2,column=0,columnspan=7)
    
    # start over at row 4 in this frame
    btn1 = Button(buttonFrame,text="1",command = lambda: addDigit('1'),width=4,bg='light blue',font=('Calibri 18'))
    btn1.grid(row=0,column=0,padx=10,pady=5)
    btn2 = Button(buttonFrame,text="2",command = lambda: addDigit('2'),width=4,bg='light blue',font=('Calibri 18'))
    btn2.grid(row=0,column=1,padx=10,pady=5)
    btn3 = Button(buttonFrame,text="3",command = lambda: addDigit('3'),width=4,bg='light blue',font=('Calibri 18'))
    btn3.grid(row=0,column=2,padx=10,pady=5)
    btn4 = Button(buttonFrame,text="4",command = lambda: addDigit('4'),width=4,bg='light blue',font=('Calibri 18'))
    btn4.grid(row=0,column=3,padx=10,pady=5)
    btn5 = Button(buttonFrame,text="5",command = lambda: addDigit('5'),width=4,bg='light blue',font=('Calibri 18'))
    btn5.grid(row=0,column=4,padx=10,pady=5)
    btn6 = Button(buttonFrame,text="6",command = lambda: addDigit('6'),width=4,bg='light blue',font=('Calibri 18'))
    btn6.grid(row=0,column=5,padx=10,pady=5)    
    btn7 = Button(buttonFrame,text="7",command = lambda: addDigit('7'),width=4,bg='light blue',font=('Calibri 18'))
    btn7.grid(row=1,column=0,padx=10,pady=5)
    btn8 = Button(buttonFrame,text="8",command = lambda: addDigit('8'),width=4,bg='light blue',font=('Calibri 18'))
    btn8.grid(row=1,column=1,padx=10,pady=5)
    btn9 = Button(buttonFrame,text="9",command = lambda: addDigit('9'),width=4,bg='light blue',font=('Calibri 18'))
    btn9.grid(row=1,column=2,padx=10,pady=5)
    btn0 = Button(buttonFrame,text="0",command = lambda: addDigit('0'),width=4,bg='light blue',font=('Calibri 18'))
    btn0.grid(row=1,column=3,padx=10,pady=5)
    btndot = Button(buttonFrame,text=".",command = lambda: decimal(),width=4,bg='light blue',font=('Calibri 18'))
    btndot.grid(row=1,column=4,padx=10,pady=5)
    btnClear = Button(buttonFrame,text="C",command = lambda: clear(),width=4,bg='light blue',font=('Calibri 18'))
    btnClear.grid(row=1,column=5,padx=10,pady=5)
      
    amtA = StringVar()  
    amtToConvert = Label(window,textvariable = amtA, width=20, bg="black", fg="white", font=('Calibri 12'))
    amtToConvert.grid(row=3,column=0,columnspan=3,pady=20)
    
    amtB = StringVar()
    convertedAmount = Label(window,textvariable = amtB, width=20, bg="black", fg="white", font=('Calibri 12'))
    convertedAmount.grid(row=3,column=4,columnspan=3,pady=20)
    
    countryFrom.selection_set(first=0)
    countryTo.selection_set(first = 0)
    exchangeRateDict = scrapeCurrencies()
    # open output file
    outFile = open('shitter.txt','w')
    exchangeRates = [x['value'] for x in exchangeRateDict['data'].values()]
    # write exchangeRateDict to file
    outFile.write(str(exchangeRateDict))
    outFile.close()
    print(exchangeRates)
    # print(exchangeRateDict)
    # print(f'\n\n\n\n\n{countryDict}')
    window.mainloop()
    
main()
    
    
