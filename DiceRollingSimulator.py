#Importing the required libraries
import tkinter
from PIL import Image, ImageTk
import random


#Building top-level widget
root = tkinter.Tk()
root.geometry('400x400')
root.title("Dice Rolling Simulator")


#Adding Labels into the frame
BlankLine = tkinter.Label(root, text= "")
BlankLine.pack()

#adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text= "Hello there!", fg= "light green", bg= "dark green", font= "Helvetica 16 bold italic")
HeadingLabel.pack()

#Images
dice = ['Images\dice-1.png', 'Images\dice-2.png', 'Images\dice-3.png', 'Images\dice-4.png', 'Images\dice-5.png', 'Images\dice-6.png']

#Simulating dice with random numbers from 0-6
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#Construct a label widget for image
ImageLabel = tkinter.Label(root, image= DiceImage)
ImageLabel.image = DiceImage

#Packing a widget in the parent widget
ImageLabel.pack(expand= True)


#Assigning functionality and adding button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #Updating Image
    ImageLabel.configure(image= DiceImage)
    #keep a reference
    ImageLabel.image = DiceImage


#Adding a button
button = tkinter.Button(root, text= "Roll the dice", fg= 'blue', command= rolling_dice)

#pack a widget in the parent widget
button.pack(expand= True)


#Running window
root.mainloop()