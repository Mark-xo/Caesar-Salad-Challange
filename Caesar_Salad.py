import random
import time,sys
from os import system, name
import tkinter as tk
from tkinter import *
from tkinter.font import Font

root=tk.Tk()
root.geometry("1280x606")
root.title("Caesar Salad")
root.grid()
bg = PhotoImage(file = "background.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)


count=0
LoadingFont=Font(family="VCR OSD Mono", size=30)
blank=tk.Label(root,text="",bg="#0b0c0b",fg="#69b183")
blank.pack(pady=12,padx=200,side=LEFT)
while(count<10):
    x=tk.Label(root, text='#',bg = "#0b0c0b",fg = "#69b183",font = LoadingFont)
    x.pack(pady=15,side=LEFT,padx =10)
    root.update() # allow window to catch up
    time.sleep(0.1)
    count += 1


labelb = Label( root, image = bg)
labelb.place(x = 0, y = 0)


myFont=Font(family="VCR OSD Mono", size=30)
label2 = Label( root, text = "CAESAR SALAD",bg = "#0b0c0b",fg = "#69b183",font = myFont)
label2.place(x = 520, y = 150)

myFont1=Font(family="VCR OSD Mono", size=15)
label3 = Label( root, text = "The Great Julius Caesar has presented his 1100 soldiers with a bowl of salad",bg = "#0b0c0b",fg = "#69b183",font = myFont1)
label3.place(x = 200, y = 220)

label4=Label(root,text="You have been given one of the bowl, can you solve the mystery and save the tux",bg="#0b0c0b",fg="#69b183",font=myFont1)
label4.place(x=185,y=250)
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )

a=random.randint(1,303)
print(a)
with open('salad.txt', 'r',encoding='utf-8') as f:
    line=f.readlines()[a]
    f.close()
    w=line.split()[0]
    print (w)
    line=line.replace(w,'',1)
    print (line)
    # encrypt the line in caesar cipher
    key = 12
    cipher = ''
    for char in line:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + key - 97) % 26 + 97)
global out


def Submission():
    Submit.place(x=740,y=445)
    root.update()


def takeInput():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT != w):
        inputtxt.delete("1.0", "end-1c")
        output=tk.Label(root,text="Incorrect! TRY AGAIN",bg="#0b0c0b",fg="#69b183",font=myFont2)
        output.place(x=500,y=520)
        root.update()
        time.sleep(3)
        output.destroy()
        root.update()
        time.sleep(1)
        # inputtxt.pack_forget()
        Submit.pack_forget()
        Submission()
    else:
        output=tk.Label(root,text="Correct!",bg="#0b0c0b",fg="#69b183",font=myFont2)
        output.place(x=500,y=520)
        root.update()
        time.sleep(1)
        root.destroy()

    
CipherFont=Font(family="VCR OSD Mono", size=15)

label5=Text(root,height=4,bg = "#0b0c0b",fg = "#69b183",font=CipherFont,bd=2)
label5.insert(1.0,cipher)
label5.place(x = 200, y = 310)
label5.configure(state="disabled")

myFont2=Font(family="VCR OSD Mono", size=17)
label6 = Label(text = "What is your answer? ",bg = "#0b0c0b",fg = "#69b183",font = myFont2)
label6.place(x = 200, y = 410)

TextBox=PhotoImage(file = "TextBox.png")
TextBOX = Label( root, image = TextBox,bd=0)
TextBOX.place(x = 300, y = 440)

inputtxt = Text(root, height = 1.4,width = 40,bg = "#0b0c0b",fg = "#69b183",bd=0)
inputtxt.configure(font=("VCR OSD Mono", 15),insertbackground="white",insertwidth=1)
inputtxt.place(x = 330, y = 460)

Submit=Button(root,text="Submit",bg="#0b0c0b",fg="#69b183",font=myFont1,command=lambda:takeInput(),bd=0)
button=PhotoImage(file="button.png")
Submit.config(image=button)

inputtxt.bind("<Return>", lambda event: takeInput())

Submission()

root.mainloop()