from tkinter import * 
import tkinter
window= tkinter.Tk() 
root = tkinter 
import webbrowser
import customtkinter
#ws = Tk()
window.title('Dashboard')
window.geometry('1280x720')

canvas = Canvas(
    window,
    width = 223, 
    height = 200,
    bg='black'
    )      
canvas.place(x=540,y=0) 
#canvas.pack(fill=X)   
canvas.config(bg='black')  
#img = PhotoImage(file="C:\\Users\\saiye\\OneDrive\\Pictures\\ook.png")      
img = PhotoImage(file="C:\\Users\\saiye\\OneDrive\\Desktop\\icon.png")
canvas.create_image(
    10,
    10, 
    anchor=NW, 
    image=img
    )  



lbl_title=Label(window,text="Menu      ")
lbl_title.config(font=('Helvetica bold', 40,"bold"),fg="black",width=10)
lbl_title.place(x=0,y=200)
#lbl_title.pack(fill=X)


pall_magnize_Button = tkinter.Button(text="Pall Magnize      ",fg="Black",font='30',width=15,bg="#769ADD")
pall_magnize_Button.place(x=50,y=280)

pall_magnize_Button = tkinter.Button(text="My First Scribble",fg="Black",font='15',width=15,bg="#769ADD")
pall_magnize_Button.place(x=50,y=330)

pall_magnize_Button = tkinter.Button(text="Data                 ",fg="Black",font='15',width=15,bg="#769ADD")
pall_magnize_Button.place(x=50,y=380)

pall_magnize_Button = tkinter.Button(text="School Daries    ",fg="Black",font='15',width=15,bg="#769ADD")
pall_magnize_Button.place(x=50,y=430)

pall_magnize_Button = tkinter.Button(text="Packages           ",fg="Black",font='15',width=15,bg="#769ADD")
pall_magnize_Button.place(x=50,y=480)

def callback(url):
    webbrowser.open_new(url)

#window = Tk()
link1 = Label(window, text="INSTRAGRAM", fg="blue", cursor="hand2",font=20)
link1.place(x=280,y=565)
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

link2 = Label(window, text="FACKBOOK", fg="blue", cursor="hand2",font=20)
link2.place(x=480,y=565)
link2.bind("<Button-1>", lambda e: callback("http://www.facebook.com"))

link2 = Label(window, text="GMAIL", fg="blue", cursor="hand2",font=20)
link2.place(x=650,y=565)
link2.bind("<Button-1>", lambda e: callback("http://www.gmail.com"))

lbl_title=Label(window,text="Contact us:")
lbl_title.config(font=('Helvetica bold', 30,"bold"),fg="black",width=10)
lbl_title.place(x=0,y=550)

def button_callback():
    print("button pressed")

button = customtkinter.CTkButton(window, text="    Pall Magzine(Entries)    ",command=button_callback,width=200,height=100,font=('bold',30))
button.place(x=400,y=280)

button = customtkinter.CTkButton(window, text="  My First Scribble(Entries)",command=button_callback,width=200,height=100,font=('bold',30))
button.place(x=900,y=280)

button = customtkinter.CTkButton(window, text="  School Daries(Entrires)  ",command=button_callback,width=200,height=100,font=('bold',30))
button.place(x=400,y=430)

button = customtkinter.CTkButton(window, text="  Packages(Entries)            ",command=button_callback,width=200,height=100,font=('bold',30))
button.place(x=900,y=430)

window.mainloop()