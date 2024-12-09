from tkinter import *
import sqlite3
db=sqlite3.connect("ticket.db")
try:
       cr=db.cursor()
       cr.execute("create table ticket(Name text,Contact integer,No_of_Infants integer,No_of_Adult integer,No_of_Baggages integer,Total_no_of_Passengers integer,Pakistan_ticket integer,US_ticket integer)")
       db.commit()
except:
        print("Successfully Submitted!!!")
w=Tk()
"""
#declaring global variable
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()
k=StringVar()
l=StringVar()
m=StringVar()
n=StringVar()
o=StringVar()
p=StringVar()
q=StringVar()
r=StringVar()
s=StringVar()
t=StringVar()
u=StringVar()
v=StringVar()
x=StringVar()
y=StringVar()
z=StringVar()
"""
w.geometry("600x600")
w.config(background="steel blue")
w.state("zoomed")
w.title("safe airlines")

#creating frame1
frame1=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame1.place(x=10,y=10,height=80,width=1510)

#book your flight label
book=Label(frame1,text="BOOK YOUR TICKET",font=("elephant",25,"bold"),bg="black",fg="white")
book.place(x=570,y=15)

#creating frame2
frame2=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame2.place(x=10,y=100,height=110,width=1510)

#passenger details
pas=LabelFrame(frame2,text="PASSENGER DETAILS:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
pas.place(x=20,y=5,height=90,width=1470)

#name
name=Label(frame2,text="May I know your good name please...?",font=("times new roman",16,"bold"),bg="black",fg="white")
name.place(x=30,y=35)

#entry box for name
e1=Entry(frame2,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=a)
e1.place(x=388,y=33)

#contact
no=Label(frame2,text="Contact No.",font=("times new roman",16,"bold"),bg="black",fg="white")
no.place(x=720,y=35)

#entry box for contact no
e2=Entry(frame2,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=b)
e2.place(x=850,y=33)

#date
date=Label(frame2,text="Date.",font=("times new roman",16,"bold"),bg="black",fg="white")
date.place(x=1180,y=35)

#entry box for date
e23=Entry(frame2,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=c)
e23.place(x=1250,y=33,width=200)


#creating frame3
frame3=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame3.place(x=10,y=220,height=400,width=500)

#Passenger travel details
pas1=LabelFrame(frame3,text="PASSENGER TRAVEL DETAILS:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
pas1.place(x=13,y=5,height=380,width=470)

#infants
infants=Label(frame3,text="No. of Infants-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
infants.place(x=25,y=45)

#entry box for infants
e3=Entry(frame3,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=d)
e3.place(x=270,y=40,width=200)

#adults
adult=Label(frame3,text="No. of Adults-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
adult.place(x=25,y=95)

#entry box for agults
e4=Entry(frame3,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=e)
e4.place(x=270,y=90,width=200)
#baggages
baggages=Label(frame3,text="No of Baggages-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
baggages.place(x=25,y=145)
#entry box for baggages
e5=Entry(frame3,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=f)
e5.place(x=270,y=140,width=200)

#total passengers
total=Label(frame3,text="Total No. of Passengers-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
total.place(x=25,y=195)

#entry box for total passengers
e6=Entry(frame3,font=("times new roman",22,"bold"),bg="lightgray",bd=3)#,textvar=g)
e6.place(x=270,y=190,width=200)

#creating frame4
frame4=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame4.place(x=520,y=220,height=400,width=500)


#number of tickets to
tic=LabelFrame(frame4,text="NUMBER OF TICKETS TO:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
tic.place(x=13,y=5,height=380,width=470)

#Pakistan
pak=Label(frame4,text="Pakistan-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
pak.place(x=30,y=45)

#pak entry box
e6=Entry(frame4,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=h)
e6.place(x=250,y=40,height=40,width=200)


#United States
us=Label(frame4,text="United States-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
us.place(x=30,y=95)

#US entry box
e7=Entry(frame4,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=i)
e7.place(x=250,y=90,height=40,width=200)


#china
ch=Label(frame4,text="China-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
ch.place(x=30,y=145)

#China entry box
e8=Entry(frame4,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=j)
e8.place(x=250,y=140,height=40,width=200)

#Maldives
mal=Label(frame4,text="Maldives-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
mal.place(x=30,y=195)

#Maldives entry box
e9=Entry(frame4,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=k)
e9.place(x=250,y=190,height=40,width=200)

#Russia
rus=Label(frame4,text="Russia-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
rus.place(x=30,y=245)

#Russia entry box
e10=Entry(frame4,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=l)
e10.place(x=250,y=240,height=40,width=200)

#Australia
aus=Label(frame4,text="Australia-",font=("times new roman",16,"bold"),bg="black",fg="powderblue")
aus.place(x=30,y=295)

#Australia entry box
e11=Entry(frame4,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=m)
e11.place(x=250,y=290,height=40,width=200)


#creating frame5
frame5=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame5.place(x=1030,y=220,height=400,width=490)

#refreshments in flight
food=LabelFrame(frame5,text="REFRESHMENTS IN FLIGHT:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
food.place(x=13,y=5,height=380,width=459)

#veg
veg=Label(frame5,text="Vegeterian meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
veg.place(x=25,y=40)

#Veg entry box
e12=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=n)
e12.place(x=250,y=40,height=40,width=200)

#nonveg
nonveg=Label(frame5,text="Non-Vegeterian meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
nonveg.place(x=25,y=90)

#Non-Veg entry box
e13=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=o)
e13.place(x=250,y=90,height=40,width=200)

#vegan 
vegan=Label(frame5,text="Vegan meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
vegan.place(x=25,y=140)

#Vegan entry box
e14=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=p)
e14.place(x=250,y=140,height=40,width=200)

#gluten-free 
glu=Label(frame5,text="Gluten-free meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
glu.place(x=25,y=190)

#gluten entry box
e15=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=q)
e15.place(x=250,y=190,height=40,width=200)

#diabetic-free 
dia=Label(frame5,text="Diabetic meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
dia.place(x=25,y=240)

#Diabetic entry box
e16=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=r)
e16.place(x=250,y=240,height=40,width=200)

#baby meal 
baby=Label(frame5,text="Baby meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
baby.place(x=25,y=290)

#baby entry box
e17=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=s)
e17.place(x=250,y=290,height=40,width=200)

#creating frame 6
frame6=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame6.place(x=10,y=630,height=150,width=1510)
#ticket details
tic1=LabelFrame(frame6,text="TICKET DETAILS:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
tic1.place(x=20,y=5,height=130,width=1470)

#passenger ticket price
ticprice=Label(frame6,text="Passenger Ticket Price",font=("times new roman",16,"bold"),bg="black",fg="white")
ticprice.place(x=30,y=35)

#entry box for passenger ticket price
e18=Entry(frame6,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=t)
e18.place(x=300,y=30,height=30,width=200)

#visa price
vprice=Label(frame6,text="Visa Price",font=("times new roman",16,"bold"),bg="black",fg="white")
vprice.place(x=30,y=68)

#entry box for visa price
e19=Entry(frame6,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=u)
e19.place(x=300,y=63,height=30,width=200)

#total refreshment price
fprice=Label(frame6,text="Total Refreshments Price",font=("times new roman",16,"bold"),bg="black",fg="white")
fprice.place(x=30,y=100)

#entry box for refreshment price
e20=Entry(frame6,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=v)
e20.place(x=300,y=96,height=30,width=200)

#Travel tax
ttax=Label(frame6,text="Travel Tax",font=("times new roman",16,"bold"),bg="black",fg="white")
ttax.place(x=540,y=35)

#entry box for Travel tax
e20=Entry(frame6,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=w)
e20.place(x=710,y=35,height=30,width=200)

#IGST tax
itax=Label(frame6,text="IGST Tax",font=("times new roman",16,"bold"),bg="black",fg="white")
itax.place(x=540,y=68)

#entry box for IGST tax
e21=Entry(frame6,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=x)
e21.place(x=710,y=68,height=30,width=200)

#Value added tax
vtax=Label(frame6,text="Value Added Tax",font=("times new roman",16,"bold"),bg="black",fg="white")
vtax.place(x=540,y=100)

#entry box for value added tax
e22=Entry(frame6,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3)#,textvar=y)
e22.place(x=710,y=101,height=30,width=200)
"""
#data insertion
def submit():
    ae=a.get()
    be=b.get()
    ce=c.get()
    de=d.get()
    ee=e.get()
    fe=f.get()
    ge=g.get()
    he=h.get()
    ie=i.get()
    je=j.get()
    ke=k.get()
    le=l.get()
    me=m.get()
    ne=n.get()
    oe=o.get()
    pe=p.get()
    qe=q.get()
    re=r.get()
    se=s.get()
    te=t.get()
    ue=u.get()
    ve=v.get()
    we=w.get()
    xe=x.get()
    ye=y.get()
    '''
    
    cr.execute("insert into ticket(No_of_Infants,No_of_ghch_,No_of_Baggages,)values(?,?,?)",(ae,be,ce))
    db.commit()
    print("Data is inserted Successfully")
    ae=a.set("")
    be=b.set("")
    ce=c.set("")
  #  d=s.set("")

"""
#submit button
sbutton=Button(frame6,text="Submit",font=("britannic bold",16,"bold"),bg="blue",fg="white")
sbutton.place(x=920,y=33,height=90,width=135)

#generate bill button
gbutton=Button(frame6,text="Generate Bill",font=("britannic bold",16,"bold"),bg="green",fg="white",)
gbutton.place(x=1060,y=33,height=90,width=138)

#clear button
cbutton=Button(frame6,text="Clear",font=("britannic bold",16,"bold"),bg="purple",fg="white",)
cbutton.place(x=1205,y=33,height=90,width=135)

#exit button
ebutton=Button(frame6,text="Exit",font=("britannic bold",16,"bold"),bg="red",fg="white",)
ebutton.place(x=1348,y=33,height=90,width=135)

w.mainloop()
