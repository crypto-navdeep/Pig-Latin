# Importing Modules
from tkinter import Tk, Label, Button, StringVar, Entry, Frame
from win32api import GetSystemMetrics
import webbrowser
import ctypes

#Increasing the DPI settings
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)

# Some lines added, by Navdeep

EXCEPTIONS = {	
    "honest":"honestyay",
}

# Lines added by Navdeep, Over.

root = Tk()
root.title("Pig Latin")

WIDTH, HEIGHT = GetSystemMetrics(0)*2//3, GetSystemMetrics(0)//3
root.geometry(f"{WIDTH}x{HEIGHT}")
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
root.config(bg = "black")

hu = HEIGHT/1000
wu = WIDTH/1000

# This Function is added by navdeep.


def convertToPigLatin(sentence):	
    #Format the the sentence	
    original = sentence.strip().lower()	

    # split sentence into words	
    words = original.split()	

    # loop through words and convert to pig latin	
    newWords = []	

    for word in words:	
        if word in EXCEPTIONS:newWords.append(EXCEPTIONS[word])	
        # if word starting with vowel	
        elif word[0] in "aeiou":	
            if word[-1] != "y":newWord = word + "yay"	
            else:newWord = word + "ay"	
            newWords.append(newWord)	
        # if word not starting with a vowel	
        else:	
            #Get the first vowel position	
            vowelPos = 0	
            for letter in word:	
                if letter not in "aeiou":	
                    vowelPos = vowelPos + 1	
                else:	
                    break	

            #Convert it from there	
            cons = word[:vowelPos]	
            theRest = word[vowelPos:]	
            new_word = theRest + cons + "ay"	
            newWords.append(new_word)	

    # stick words back together	
    output = " ".join(newWords) 	

    return output


def convert(event = None):
    if inputEntry.get().count(" ") == len(inputEntry.get()):return
    global converted
    converted.place_forget()
    
    converted = Label(root, text = convertToPigLatin(inputEntry.get()), width = int(wu*17), bg = "lightblue", fg = "black", font = ("", int(25)))
    converted.place(x = 0, y = int(450*hu), height = hu*250, width = WIDTH)


inputEntry = StringVar()
inputBox = Entry(root, textvariable = inputEntry, justify = "center", width = int(wu*16), font = ("", int(25)))
inputBox.place(x = WIDTH*2.5/100, y = int(50*hu), width = WIDTH*95/100, height = hu*125)

button = Button(root, width = int(wu*16), text = "Convert", bg = "red", fg = "black", font = ("", int(25)), command = convert)
button.place(x = 0, y = int(225*hu), width = WIDTH, height = 225*hu)

converted = Label(root, text = "Here goes Pig-Latin", bg = "lightblue", fg = "black", font = ("", int(23)))
converted.place(x = 0, y = int(450*hu), height = hu*250, width = WIDTH)
root.bind("<Return>",convert)

# This function shows the creators

def showCreators():
    win = Frame(root, bg = "black")
    win.place(x = 0, y = 0, width = WIDTH, height = HEIGHT)

    Label(win, text = "About The Creators", font = (" ", int(30)), fg = "white", bg = "black").place(x = WIDTH//2, y = hu*100, anchor = "center")

    string = """
    The first version of this project was created by 
    Navdeep K, assisted by Ved Rathi. 
    """

    Label(win, text = string, font = (" ", int(20)), justify = "left").place(x = WIDTH//2, y = HEIGHT//2, anchor = "center")
    Button(win, text = "Go Back", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : win.place_forget()).place(x = 0, y = 0)
    Button(win, text = "Ved's Github", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/Ved-programmer")).place(x = 150*wu, y = 800*hu, width = 250*wu)
    Button(win, text = "Navdeep's Github", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/crypto-navdeep")).place(x = 600*wu, y = 800*hu, width = 250*wu)

# This function is going to tell about the pig latin

def showAbout():
    win = Frame(root, bg = "black")
    win.place(x = 0, y = 0, width = WIDTH, height = HEIGHT)

    Label(win, text = "About Pig Latin", font = (" ", int(30)), fg = "white", bg = "black").place(x = WIDTH//2, y = hu*100, anchor = "center")

    string = """
    Pig Latin is a language game or argot in which English words are altered, 
    usually by adding a fabricated suffix or by moving the onset or initial 
    consonant or consonant cluster of a word to the end of the word and adding
    a vocalic syllable to create such a suffix. For example, "Wikipedia" would
    become "Ikipediaway" (the "W" is moved from the beginning and has "ay" 
    appended to create a suffix). The objective is to conceal the words from 
    others not familiar with the rules. The reference to Latin is a deliberate
    misnomer; Pig Latin is simply a form of argotor jargon unrelated to Latin, 
    and the name is used for its English connotations as a strange and 
    foreign-sounding language. It is most often used by young children as a 
    fun way to confuse people unfamiliar with Pig Latin.
    """

    Label(win, text = string, font = (" ", int(13)), justify = "left").place(x = WIDTH//2, y = HEIGHT//2, anchor = "center")
    Button(win, text = "Go Back", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : win.place_forget()).place(x = 0, y = 0)
    Button(win, text = "View on Github", font = (" ", int(15)), justify = "center", bg = "red", command = lambda : webbrowser.open("https://github.com/crypto-navdeep/Pig-Latin")).place(x = WIDTH//2-100*wu, y = HEIGHT - 200*hu, width = 200*wu)
    



def createButton(Text, Command, X):
    button = Button(root, command = Command, text = Text, width = int(wu*10), bg = "yellow", font = ("", int(20)))
    button.place(x = X, y = int(750*hu), height = hu*200, width = wu*300)
    return button

creatorButton = createButton("Creators", showCreators ,int(100*wu))
aboutButton = createButton("About", showAbout, int(600*wu))

root.mainloop()

# End
'''
Pig Latin Desktop Python GUI
 * Copyright 2021 Ved Rathi
 * Licensed under MIT (https://github.com/crypto-navdeep/Pig-Latin/blob/master/LICENSE)
'''