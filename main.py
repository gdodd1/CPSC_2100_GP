from tkinter import *
import pickle
from PIL import Image, ImageTk
#import scrape function from scrape.py located in code folder
# from code.scrape import scrape
#create tkinter window

#read currencies.dat using pickle
with open('code/currencies.dat', 'rb') as file:
    currencies = pickle.load(file)

countries = [k for k in currencies.keys()]
print(currencies)

root = Tk()
root.title("Exchange Rate Calculator")
root.geometry("500x500")
root.resizable(False, False)

# when the window opens, run the scrape function
# data = scrape()
# when defining tkinter widgets, use rows and cols to place them
#make header label, with blk background and white text
header = Label(root, text="Exchange Rate Calculator", bg="black", fg="white", font=("Arial", 24))
header.pack(fill=X) #fill X axis

#make list of countries
left_country_list = Listbox(root, bg="white", fg="black", font=("Arial", 16), selectmode=SINGLE)
right_country_list = Listbox(root, bg="white", fg="black", font=("Arial", 16), selectmode=SINGLE)

#loop through countries and add them to list
for country in countries:
    left_country_list.insert(END, country)
    right_country_list.insert(END, country)

# print the country when clicked
def print_country(event):
    selection = left_country_list.curselection()
    if selection:
        print(f'Left: {left_country_list.get(selection)}')
def pc2(event):
    selection = right_country_list.curselection()
    if selection:
        print(f'Right: {right_country_list.get(selection)}')
#bind the print_country function to the listbox
left_country_list.bind("<<ListboxSelect>>", print_country)
right_country_list.bind("<<ListboxSelect>>", pc2)

# pack the listbox side by side
left_country_list.pack(side=LEFT, fill=BOTH, expand=True)
right_country_list.pack(side=RIGHT, fill=BOTH, expand=True)


#TODO: get flags on screen
#TODO: numbers and decimal point
#TODO: logic to not put a second decimal point
#TODO: logic for pulling data from gui, convert into float, and multiply by exchange rate


#keep window open until closed
root.mainloop()