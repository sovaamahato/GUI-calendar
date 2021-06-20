from tkinter import *
import calendar
from tkinter import messagebox


text=calendar.calendar(2021)


win=Tk()
win.title("calender")
win.configure(bg="skyblue")
win.geometry("900x650+200+40")
win.resizable(False,False)

yy=2021




def action():
    
    var1=int(entryvar.get())
    
    if var1<1 or var1>12:
        messagebox.showerror("Error","please enter valid months")
    date =calendar.month(yy,var1)
    
    monthtextbox.insert(END, date)
    
        

    


label1=Label(win, text="welcome to the Calendar app", width=400, bg="light green", font=('chiller',20,'bold'), relief=GROOVE,bd=3)
label1.pack(pady=10)

choiceEntry=Label(win,bg='skyblue', text="Enter the month: ", font=('chiller',20,'bold'))
choiceEntry.place(x=10,y=70)


#################-------------Enrtybox----------------------
entryvar=StringVar()
entrybox=Entry(win,bg="light green", font=('ariel',15,'bold') , width=10 ,textvariable=entryvar)
entrybox.place(x=190, y=70)
entrybox.focus()

###################--------------button---------------

button1=Button(win, bg="green",text="Click here", font=('ariel',15,'bold'),activebackground="green" , activeforeground="white",command=action )
button1.place(x=100, y=120,width=150)

###################----------------------------------------------Frame------------------------------------------
calendarframe=Frame(win, bg='light green',relief=GROOVE,bd=5)
calendarframe.place(x=340, y=55, height=590, width=540)


monthframe=Frame(win, bg='light green',relief=GROOVE,bd=5)
monthframe.place(x=10, y=180, height=400, width=310)

#####################-----------------------------------------calender codes------------------------------------------------
calLabel=Label(calendarframe, bg="light green",text=text, font="Consoles 11")
calLabel.grid(row=1, column=1, padx=10)

monthtextbox=Text(win, bg='light green',fg='red' ,relief=FLAT, font=('ariel',15,'bold'))
monthtextbox.place(x=13, y=190, height=240, width=300)

todaysdate=Label




win.mainloop()



