import tkinter
from tkinter import *
window= tkinter.Tk()
from tkinter import ttk


#import tkinter.tix as tix
#root = tix.Tk()
root = tkinter

window.title("DATA")#.title is used to title a software
window.geometry("1280x720")#.geometry is used to set the height,weidth, and x,y axis of gui.
window.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
window.focus_force()

var__first_name_entry=StringVar()
lbl_title=Label(window,text="DATA")
lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
lbl_title.place(x=580,y=0)
lbl_title.pack(fill=X)



fram = tkinter.Frame(window,bg="#324370")
fram.place(x=50,y=150)



#saving user info
user_info_frame = tkinter.LabelFrame(fram, text ="User Information",bg="#324370",fg="#FFFFFF",font='50')
user_info_frame.pack(padx=5,pady=5)

first_name_label = tkinter.Label(user_info_frame, text="First Name",bg="#324370",fg="#FFFFFF",font='30',width=20)
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame, text= "Last Name",bg="#324370",fg="#FFFFFF",font='30')
last_name_label.grid(row=1,column=0)

var__first_name_label=StringVar()




first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=0,column=1,padx=10,pady=10)
last_name_entry.grid(row=1,column=1,padx=10,pady=10)

age_label = tkinter.Label(user_info_frame,text="Age          ",bg="#324370",fg="#FFFFFF",font='30')
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=110,width='18')
age_label.grid(row=2,column=0)
age_spinbox.grid(row=2,column=1,padx=5,pady=10)

contact_label = tkinter.Label(user_info_frame, text="Contact no",bg="#324370",fg="#FFFFFF",font='30')
contact_label.grid(row=3,column=0)
contact_entry = tkinter.Entry(user_info_frame,width=20)
contact_entry.grid(row=3,column=1,padx=10,pady=10)


occup_label = tkinter.Label(user_info_frame, text="Occupation",bg="#324370",fg="#FFFFFF",font='30')
occup_label.grid(row=4,column=0)
occup_entry = tkinter.Entry(user_info_frame)
occup_entry.grid(row=4,column=1,padx=10,pady=10)


addr_label = tkinter.Label(user_info_frame, text="Address    ",bg="#324370",fg="#FFFFFF",font='30')
addr_label.grid(row=5,column=0)
addr_entry = tkinter.Entry(user_info_frame)
addr_entry.grid(row=5,column=1,padx=10,pady=10)




fram2 = tkinter.Frame(window,bg="#324370")
fram2.place(x=450,y=150)


user_info_frame2 = tkinter.LabelFrame(fram2, text ="Social Media Links",bg="#324370",fg="#FFFFFF",font='50',)
user_info_frame2.pack(padx=10,pady=10)

insta_label = tkinter.Label(user_info_frame2, text="Instagram  ",bg="#324370",fg="#FFFFFF",font='30',width=21)
insta_label.grid(row=6,column=0)
insta_entry = tkinter.Entry(user_info_frame2)
insta_entry.grid(row=6,column=1,padx=10,pady=10)



fb_label = tkinter.Label(user_info_frame2, text="Facebook  ",bg="#324370",fg="#FFFFFF",font='30')
fb_label.grid(row=7,column=0)
fb_entry = tkinter.Entry(user_info_frame2)
fb_entry.grid(row=7,column=1,padx=10,pady=10)


fb_label = tkinter.Label(user_info_frame2, text="Other        ",bg="#324370",fg="#FFFFFF",font='30')
fb_label.grid(row=8,column=0)
fb_entry = tkinter.Entry(user_info_frame2)
fb_entry.grid(row=8,column=1,padx=10,pady=10)

login_button = tkinter.Button(window,text="Submit")
login_button.place()


#button
Button = tkinter.Button(fram2,text="Enter Data",fg="Black",font='12',width=10)
Button.pack()


#B_Button = tkinter.Button(text="Back",fg="#FFFFFF",font='12',width=8,bg="#769ADD")
#B_Button.place(x=10,y=105)

class Clientsclass:
    def __init__(self,root):
        self.root=root
        self.back_button = Button(self.root, text="Back",command=self.on_back_button_click,bg=("#769ADD"),fg=("#FFFFFF"),font=(20))
        self.back_button.place(x=30,y=120)
        self.root.focus_force() 
     
     
     
    back_button = tkinter.Button(text="Back",fg="#FFFFFF",font='12',width=8,bg="#769ADD")
    back_button.place(x=10,y=105)
     
     
     
    def on_back_button_click(self):
        self.root()
 


reset_Button = tkinter.Button(text="Clear All",fg="Black",font='12',width=8)
reset_Button.place(x=1050,y=250)

reset_Button = tkinter.Button(text="Edit",fg="Black",font='12',width=8)
reset_Button.place(x=1050,y=350)


reset_Button = tkinter.Button(text="Delete",fg="Black",font='12',width=8)
reset_Button.place(x=1050,y=450)



search = tkinter.Frame(window,bg="#324370")
search.pack(fill="x")







search_label = tkinter.Label(bg="#324370",fg="#FFFFFF",font='30')
search_box = ttk.Combobox(width='15',values=['First Name','Last Name','Age'])
search_label.place(x=1050,y=140)
search_box.place(x=1050,y=140)

search_entry = tkinter.Entry(width=17)
search_entry.place(x=1050,y=160)

reset_Button = tkinter.Button(text="Search",fg="Black",width=5,)
reset_Button.place(x=1050,y=180)


se_label = tkinter.Label( text="Search",bg="#324370",fg="#FFFFFF",font='30')
se_label.place(x=1050,y=110)

 
###################################  data view
user_frame= tkinter.Frame(window,bd=3)
user_frame.place(x=0,y=500,relwidth=1,height=150)
scrolly= Scrollbar(user_frame,orient=VERTICAL)
scrollx= Scrollbar(user_frame,orient=HORIZONTAL)

usertable= ttk.Treeview(user_frame,columns=("uid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=usertable.yview)
scrollx.config(command=usertable.xview)
usertable.heading("uid",text="UID")
usertable.heading("name",text="NAME")


usertable.column("uid",width=100)
usertable.column("name",width=100)


usertable.pack(fill=BOTH,expand=1)
 
#====================================================================================
        
        

#if __name__="__main__":
root.mainloop()
window.mainloop()#.mainloop is us