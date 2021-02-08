from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
import fileinput
from tkinter.messagebox import*

def funktion(a):
    tabs.select(a)

def open_():
    file=askopenfilename()#название файла
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file=asksaveasfile(mode='w',defaultextension=((".txt"),(".docx")),filetypes=(("Notepad","txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showninfo("No")

def imgChange(name, sample):
    tabs.select(1)
    global img
    img=PhotoImage(file=name).subsample(sample)
    can.create_image(10,10,image=img,anchor=NW)

root=Tk()
root.geometry("600x400")
root.title("Elemendid Tkinteris")

tabs=ttk.Notebook(root)
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Seitsmes","Kaheksas"]

def funktion(a):
    tabs.select(a)

def mathimatic():
    try:
        getting = ent.get()
        solve = eval(getting)
        label.configure(text=f"Vastus: {round(solve,1)}", font="Arial 15")
    except:
        label.configure(text="Error.", font="Arial 15")

#for i in range(8): #len(texts)
#   tab=Frame(tabs)
#   tabs.add(tab,text=texts[i])
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tabs.add(tab1,text=texts[0])
tabs.add(tab2,text=texts[1])
tabs.add(tab3,text=texts[2])

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator='Command+V',command=lambda:funktion(0))
m1.add_separator()
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_command(label="Tab3",command=lambda:funktion(2))

m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Salmon",command=lambda:root.config(bg="salmon"))
m2.add_command(label="Crimson",command=lambda:root.config(bg="crimson"))
m2.add_command(label="HotPink",command=lambda:root.config(bg="hotpink"))
m2.add_command(label="Coral",command=lambda:root.config(bg="coral"))
m2.add_command(label="Pink",command=lambda:root.config(bg="pink"))
m2.add_command(label="Tomato",command=lambda:root.config(bg="tomato"))
m2.add_command(label="Orange",command=lambda:root.config(bg="orange"))
m2.add_command(label="GreenYellow",command=lambda:root.config(bg="greenyellow"))
m2.add_command(label="SpringGreen",command=lambda:root.config(bg="springgreen"))
m2.add_command(label="Olive",command=lambda:root.config(bg="olive"))
m2.add_command(label="MediumAquamarine",command=lambda:root.config(bg="mediumaquamarine"))
m2.add_command(label="LightCyan",command=lambda:root.config(bg="lightcyan"))
m2.add_command(label="PaleTurquoise",command=lambda:root.config(bg="paleturquoise"))
m2.add_command(label="SteelBlue",command=lambda:root.config(bg="steelblue"))
m2.add_command(label="SkyBlue",command=lambda:root.config(bg="skyblue"))
m2.add_command(label="CornflowerBlue",command=lambda:root.config(bg="cornflowerblue"))
m2.add_command(label="RoyalBlue",command=lambda:root.config(bg="royalblue"))
m2.add_command(label="LemonChiffon",command=lambda:root.config(bg="lemonchiffon"))
m2.add_command(label="Moccasin",command=lambda:root.config(bg="moccasin"))
m2.add_command(label="Khaki",command=lambda:root.config(bg="khaki"))
m2.add_command(label="Lavender",command=lambda:root.config(bg="lavender"))
m2.add_command(label="Plum",command=lambda:root.config(bg="plum"))
m2.add_command(label="Violet",command=lambda:root.config(bg="violet"))
m2.add_command(label="BlueViolet",command=lambda:root.config(bg="blueviolet"))
m2.add_command(label="MediumPurple",command=lambda:root.config(bg="mediumpurple"))
m2.add_command(label="Silver",command=lambda:root.config(bg="silver"))
m2.add_command(label="Maroon",command=lambda:root.config(bg="maroon"))
m2.add_command(label="Thistle",command=lambda:root.config(bg="thistle"))

can=Canvas(tab2,width=300,height=200)
can.pack()

m3=Menu(M,tearoff=0)
M.add_cascade(label="Animals",menu=m3)
m3.add_command(label="Dog", command=lambda:imgChange("dog.png",10))
m3.add_command(label="Cat", command=lambda:imgChange("cat.png",5))
m3.add_command(label="Bird", command=lambda:imgChange("bird.png",3))
m3.add_command(label="Rabbit", command=lambda:imgChange("rabbit.png",7))
m3.add_command(label="Raccoon", command=lambda:imgChange("raccoon.png",2))

btn_open=Button(tab1,text="Open", command=open_)
btn_save=Button(tab1,text="Save", command=save_)
btn_exit=Button(tab1,text="Exit", command=exit_)
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

ent = Entry(tab3, width=30, font="Arial")
ent.grid(row=1, column=0, columnspan=3)
label = Label(tab3, width=20, height=5, bg="Orange")
label.grid(row=1, column=3)
button_2 = Button(tab3, text="Solve", command=mathimatic)
button_2.grid(row=2, column=2)

tabs.pack(fill="both")

root.mainloop()

