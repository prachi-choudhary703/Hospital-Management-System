from tkinter import *
from tkinter import messagebox
import sqlite3
win=Tk()
win.title("Hospital Management System")
win.geometry("750x750")
conn=sqlite3.connect("hospitaldb.db")

conn.execute("create table if not exists login(username char(30) not null,password char(30) not null)")
conn.execute("create table if not exists pinfo(pid char(30) not null,pname char(30) not null,page char(30) not null,pdisease char(30) not null,pcontact char(30) not null,pemail char(30) not null,paddress char(30) not null,pdocname char(30) not null,pslip char(30) not null)")
conn.execute("create table if not exists docinfo(doc_id char(30) not null,docname char(30) not null,specialisation char(30) not null,age char(30) not null,doccontact char(30) not null,docemail char(30) not null,docaddress char(30) not null,fees char(30) not null,salary char(30) not null)")
conn.execute("create table if not exists nurseinfo(nrs_id char(30) not null,nrsname char(30) not null,specialisation char(30) not null,age char(30) not null,nrscontact char(30) not null,nrsemail char(30) not null,nrsaddress char(30) not null,salary char(30) not null)")
conn.execute("create table if not exists workerinfo(wk_id char(30) not null,wkname char(30) not null,work char(30) not null,age char(30) not null,wkcontact char(30) not null,wkemail char(30) not null,wkaddress char(30) not null,salary char(30) not null)")
conn.execute("create table if not exists lbtest(pid char(30) not null,pname char(30) not null,pcontact char(30) not null,pdisease char(30) not null,mtest char(30) not null,pcharges char(30) not null)")
conn.execute("create table if not exists roominfo(pid char(30) not null,pname char(30) not null,pcontact char(30) not null,days char(30) not null,rmtype char(30) not null,rmcharges char(30) not null)")
conn.execute("create table if not exists totalcharges(pid char(30) not null,pname char(30) not null,pcontact char(30) not null,total char(30) not null)")
conn.execute("create table if not exists complaints(comid int primary key not null,name char(30) not null,contact char(30) not null,emailid char(50) not null,complaint char(100) not null)")
conn.execute("create table if not exists suggestions(sugid int primary key not null,name char(30) not null,contact char(30) not null,emailid char(50) not null,suggestion char(100) not null)")
conn.commit()


username=StringVar()
password=StringVar()
pid=StringVar()
pname=StringVar()
page=StringVar()
pdiseases=StringVar()
pcontact=StringVar()
pemail=StringVar()
paddress=StringVar()
pdocname=StringVar()
pslip=StringVar()
mtest=StringVar()
charges=StringVar()
compid=IntVar()
name=StringVar()
contact=StringVar()
email=StringVar()
complaint=StringVar()
sugid=IntVar()
suggestion=StringVar()
rmtype=StringVar()
days=IntVar()
rmcharges=StringVar()
total=StringVar()
docid=StringVar()
docname=StringVar()
sp=StringVar()
docage=StringVar()
doccontact=StringVar()
docemail=StringVar()
docaddress=StringVar()
docemail=StringVar()
fees=StringVar()
docms=StringVar()
nrsid=StringVar()
nrsname=StringVar()
nrsp=StringVar()
nrsage=StringVar()
nrscontact=StringVar()
nrsemail=StringVar()
nrsaddress=StringVar()
nrsemail=StringVar()
nrsms=StringVar()
wkid=StringVar()
wkname=StringVar()
wk=StringVar()
wkage=StringVar()
wkcontact=StringVar()
wkemail=StringVar()
wkaddress=StringVar()
wkemail=StringVar()
wkms=StringVar()


def patientshow():
    pmframe.grid(row=0,column=0)
    mnframe.grid_forget()

def pishow():
     piframe.grid(row=0,column=0)
     pmframe.grid_forget()
        
def upshow():
    upframe.grid(row=0,column=0)
    pmframe.grid_forget()

def delshow():
    delframe.grid(row=0,column=0)
    pmframe.grid_forget()

def searchshow():
    sframe.grid(row=0,column=0)
    pmframe.grid_forget()

def lbshow():
    lbframe.grid(row=0,column=0)
    billframe.grid_forget()

def compshow():
    comframe.grid(row=0,column=0)
    csframe.grid_forget()

def csshow():
    csframe.grid(row=0,column=0)
    mnframe.grid_forget()

def sugshow():
    sgframe.grid(row=0,column=0)
    csframe.grid_forget()

def billshow():
    billframe.grid(row=0,column=0)
    mnframe.grid_forget()

def rmshow():
    rmframe.grid(row=0,column=0)
    billframe.grid_forget()

def totalshow():
    totalframe.grid(row=0,column=0)
    billframe.grid_forget()

def empshow():
    empframe.grid(row=0,column=0)
    mnframe.grid_forget()

def dbshow():
    dbframe.grid(row=0,column=0)
    empframe.grid_forget()

def nrsshow():
    nrsframe.grid(row=0,column=0)
    empframe.grid_forget()
    
def wkshow():
    wkframe.grid(row=0,column=0)
    empframe.grid_forget()
    
 
def lgprevious():
    lgframe.grid(row=0,column=0)
    mnframe.grid_forget()

def mnprevious():
    mnframe.grid(row=0,column=0)
    pmframe.grid_forget()

def pmprevious():
    pmframe.grid(row=0,column=0)
    piframe.grid_forget()
    upframe.grid_forget()
    delframe.grid_forget()
    sframe.grid_forget()

def lbprevious():
    billframe.grid(row=0,column=0)
    lbframe.grid_forget()

def comprevious():
    csframe.grid(row=0,column=0)
    comframe.grid_forget()

def csprevious():
    mnframe.grid(row=0,column=0)
    csframe.grid_forget()

def sgprevious():
    csframe.grid(row=0,column=0)
    sgframe.grid_forget()

def rmprevious():
    billframe.grid(row=0,column=0)
    rmframe.grid_forget()

def totalprevious():
    billframe.grid(row=0,column=0)
    totalframe.grid_forget()

def billprevious():
    mnframe.grid(row=0,column=0)
    billframe.grid_forget()

def empprevious():
    mnframe.grid(row=0,column=0)
    empframe.grid_forget()

def docprevious():
    empframe.grid(row=0,column=0)
    dbframe.grid_forget()

def nrsprevious():
    empframe.grid(row=0,column=0)
    nrsframe.grid_forget()

def wkprevious():
    empframe.grid(row=0,column=0)
    wkframe.grid_forget()
    
    
def pishow():
     piframe.grid(row=0,column=0)
     pmframe.grid_forget()
    
def exit1():
    win.destroy()

#-------------------------------Login Frame------------------------------------------------------------------------------------------

lgframe=Frame(win)
lgframe.grid(row=0,column=0)

def reset():
    username.set("")
    password.set("")
    
    
def signin():
    username1=username.get()
    password1=password.get()
    if(username1==""):
        messagebox.showinfo("Hospital Management","Please Enter the username")
        
    elif(password1==""):
        messagebox.showinfo("Hospital Management","please Enter the password")
    else:
        cursor=conn.execute("select * from login where username=? and password=?",(username1,password1,))
        if cursor.fetchone() is None:
            messagebox.showinfo("Hospital Management","Please Enter the right username and password")
        else:
            messagebox.showinfo("Hospital Management","You are administrator of project")
            mnframe.grid(row=0,column=0)
            lgframe.grid_forget()
            
def signup():
    username1=username.get()
    password1=password.get()
    if(username1==""):
        messagebox.showinfo("Hospital Management","Please Enter the username")
        
    elif(password1==""):
        messagebox.showinfo("Hospital Management","please Enter the password")
    else:
        conn.execute("create table if not exists login(username char(30) not null,password char(30)not null)")
        conn.execute("insert into login values(?,?)",(username1,password1))
        conn.commit()
        messagebox.showinfo("Hospital Management","You are registered")


l1=Label(lgframe,width=22,bg='bisque',text='Hospital Management System',font=('baskerville old face',40,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=10,pady=10,ipady=13,ipadx=20)
l2=Label(lgframe,text='Username',bg='gainsboro',font=('arial',20)).grid(row=2,column=1)
t1=Entry(lgframe,textvariable=username,bd=5,font=('arial',20)).grid(row=2,column=2)
l3=Label(lgframe,text="Password",bg='gainsboro',font=('arial',20)).grid(row=3,column=1,padx=5,pady=5,ipady=3,ipadx=5)
t2=Entry(lgframe,textvariable=password,bd=5,font=('arial',20),show='*').grid(row=3,column=2)
b1=Button(lgframe,text='Signup',command=signup,bd=3,bg='royalblue',font=('arial',15,'bold'),fg='white').grid(row=7,column=1,columnspan=2,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(lgframe,text='Signin',command=signin,bd=3,bg='royalblue',font=('arial',15,'bold'),fg='white').grid(row=7,column=2,columnspan=2,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(lgframe,text='Reset',command=reset,bd=3,bg='royalblue',font=('arial',15,'bold'),fg='white').grid(row=7,column=3,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)

#-----------------------------------Main frame------------------------------------------------------------------
mnframe=Frame(win)
mnframe.grid_forget()

l1=Label(mnframe,width=22,bg='bisque',text='Hospital Management System',font=('baskerville old face',40,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=10,pady=10,ipady=13,ipadx=20)
b2=Button(mnframe,width=20,font=('arial',20,'bold'),bg='thistle',fg='purple',bd=5,text='Patient Management',command=patientshow).grid(row=1,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(mnframe,width=20,font=('arial',20,'bold'),bg='thistle',fg='purple',bd=5,text='Employee Management',command=empshow).grid(row=2,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(mnframe,width=20,font=('arial',20,'bold'),bg='thistle',fg='purple',bd=5,text='Bill Management',command=billshow).grid(row=3,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(mnframe,width=20,font=('arial',20,'bold'),bg='thistle',fg='purple',bd=5,text='Complaint and Suggetion',command=csshow).grid(row=4,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(mnframe,width=20,font=('arial',20,'bold'),bg='thistle',fg='purple',bd=5,text='Previous Page',command=lgprevious).grid(row=5,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(mnframe,width=20,font=('arial',20,'bold'),bg='thistle',fg='purple',bd=5,text='Exit',command=exit1).grid(row=6,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)

#---------------------------------------Patient Management------------------------------------------------------------------------------------
pmframe=Frame(win)
pmframe.grid_forget()

def reset1():
    pid.set("")
    pname.set("")
    page.set("")
    pdiseases.set("")
    pcontact.set("")
    pemail.set("")
    paddress.set("")
    pdocname.set("")
    pslip.set("")
    
def psave():
    pid1=pid.get()
    pname1=pname.get()
    page1=page.get()
    pdiseases1=pdiseases.get()
    pcontact1=pcontact.get()
    pemail1=pemail.get()
    paddress1=paddress.get()
    pdocname1=pdocname.get()
    pslip1=pslip.get()
    conn.execute("create table if not exists pinfo(pid char(30) not null,pname char(30) not null,page char(30) not null,pdisease char(30) not null,pcontact char(30) not null,pemail char(30) not null, paddress char(30) not null, pdocname char(30) not null, pslip char(30) not null)")
    conn.execute("insert into pinfo values(?,?,?,?,?,?,?,?,?)",(pid1,pname1,page1,pdiseases1,pcontact1,pemail1,paddress1,pdocname1,pslip1,))
    conn.commit()
    messagebox.showinfo("Patient Management","Patient information stored successfully")

def pupdate():
    pid1=pid.get()
    pname1=pname.get()
    page1=page.get()
    pdiseases1=pdiseases.get()
    pcontact1=pcontact.get()
    pemail1=pemail.get()
    paddress1=paddress.get()
    pdocname1=pdocname.get()
    pslip1=pslip.get()
    
    conn.execute("update pinfo set pname=?,page=?,pdisease=?,pcontact=?,pemail=?,paddress=?,pdocname=?,pslip=? where pid=?",(pname1,page1,pdiseases1,pcontact1,pemail1,paddress1,pdocname1,pslip1,pid1,))
    conn.commit()
    messagebox.showinfo("Patient Management","Patient Record Updated")

def psearch():
    pid1=pid.get()
    cursor=conn.execute("select * from pinfo where pid=?",(pid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Patient Management","Patient Record Not Found")
    else:
        pid.set(row[0])
        pname.set(row[1])
        page.set(row[2])
        pdiseases.set(row[3])
        pcontact.set(row[4])
        pemail.set(row[5])
        paddress.set(row[6])
        pdocname.set(row[7])
        pslip.set(row[8])
        messagebox.showinfo("Patient Management","Patient Record Searched")
            
def pdelete():
    pid1=pid.get()
    pname1=pname.get()
    conn.execute("delete from pinfo where pid=? and pname=? ",(pid1,pname1,))
    conn.commit()
    messagebox.showinfo("Patient Management","Patient Record Deleted")


def pall():
    cursor=conn.execute("select * from pinfo")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5],",",row[6],",",row[7],",",row[8])
    messagebox.showinfo("Patient Management","Please check all records in output")

l1=Label(pmframe,width=29,bg='bisque',text='Patient Management Section',font=('baskerville old face',30,'bold','underline'),fg='black',justify='center').grid(row=0,column=2,columnspan=4,padx=10,pady=10,ipady=13,ipadx=20)
b1=Button(pmframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='New Patient',command=pishow).grid(row=1,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(pmframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Update Patient Record',command=upshow).grid(row=2,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(pmframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Delete Patient Record',command=delshow).grid(row=3,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(pmframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Search Patient',command=searchshow).grid(row=4,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(pmframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='See All Patients',command=pall).grid(row=5,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(pmframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Previous Page',command=mnprevious).grid(row=6,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)                                                                                                             

piframe=Frame(win)
piframe.grid_forget()

l1=Label(piframe,width=20,bg='powderblue',text='Patient Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(piframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(piframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(piframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Age',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=page,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(piframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Diseases',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pdiseases,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(piframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Contact No',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pcontact,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(piframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pemail,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(piframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Address',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=paddress,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l9=Label(piframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Doctor Name',bd=5).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t8=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pdocname,bd=5).grid(row=8,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l10=Label(piframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Slip charges',bd=5).grid(row=9,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t9=Entry(piframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pslip,bd=5).grid(row=9,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(piframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Save',command=psave).grid(row=10,column=0)
b2=Button(piframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Reset',command=reset1).grid(row=10,column=1)
b3=Button(piframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Previous page',command=pmprevious).grid(row=10,column=2)

upframe=Frame(win)
upframe.grid_forget()


l1=Label(upframe,width=20,bg='powderblue',text='Update Patient Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(upframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(upframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(upframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Age',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=page,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(upframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Diseases',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pdiseases,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(upframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Contact No',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pcontact,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(upframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pemail,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(upframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Address',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=paddress,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l9=Label(upframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Doctor Name',bd=5).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t8=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pdocname,bd=5).grid(row=8,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l10=Label(upframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Slip charges',bd=5).grid(row=9,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t9=Entry(upframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pslip,bd=5).grid(row=9,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(upframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='update',command=pupdate).grid(row=10,column=0)
b2=Button(upframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Reset',command=reset1).grid(row=10,column=1)
b3=Button(upframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Previous page',command=pmprevious).grid(row=10,column=2)


delframe=Frame(win)
delframe.grid_forget()


l1=Label(delframe,width=20,bg='powderblue',text='Delete Patient Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(delframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(delframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(delframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(delframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(delframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Delete',command=pdelete).grid(row=10,column=0)
b2=Button(delframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Reset',command=reset1).grid(row=10,column=1)
b3=Button(delframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Previous page',command=pmprevious).grid(row=10,column=2)

sframe=Frame(win)
sframe.grid_forget()

l1=Label(sframe,width=20,bg='powderblue',text='Search Patient Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(sframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(sframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(sframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Patient Age',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=page,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(sframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Patient Diseases',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pdiseases,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(sframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Contact No',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pcontact,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(sframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pemail,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(sframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Address',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=paddress,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l9=Label(sframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Doctor Name',bd=5).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t8=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pdocname,bd=5).grid(row=8,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l10=Label(sframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Slip charges',bd=5).grid(row=9,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t9=Entry(sframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=pslip,bd=5).grid(row=9,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(sframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Search',command=psearch).grid(row=10,column=0)
b2=Button(sframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Reset',command=reset1).grid(row=10,column=1)
b3=Button(sframe,bd=5,font=('arial',15,'bold'),bg='dodgerblue',fg='white',text='Previous page',command=pmprevious).grid(row=10,column=2)

#-----------------------------------------Employee Management-------------------------------------------------------------------------

empframe=Frame(win)
empframe.grid_forget()

l1=Label(empframe,width=29,bg='bisque',text='Bill management',font=('baskerville old face',30,'bold','underline'),fg='black',justify='center').grid(row=0,column=2,columnspan=4,padx=10,pady=10,ipady=13,ipadx=20)
b1=Button(empframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Doctors',command=dbshow).grid(row=1,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(empframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Nurses',command=nrsshow).grid(row=2,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(empframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Workers',command=wkshow).grid(row=3,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(empframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Previous Page',command=empprevious).grid(row=4,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)

dbframe=Frame(win)
dbframe.grid_forget()

def docreset():
    docid.set("")
    docname.set("")
    sp.set("")
    docage.set("")
    doccontact.set("")
    docemail.set("")
    docaddress.set("")
    fees.set("")
    docms.set("")

def docsave():
    docid1=docid.get()
    docname1=docname.get()
    sp1=sp.get()
    docage1=docage.get()
    doccontact1=doccontact.get()
    docemail1=docemail.get()
    docaddress1=docaddress.get()
    fees1=fees.get()
    docms1=docms.get()
    conn.execute("create table if not exists docinfo(doc_id char(30) not null,docname char(30) not null,specialisation char(30) not null,age char(30) not null,doccontact char(30) not null,docemail char(30) not null, docaddress char(30) not null, fees char(30) not null, salary char(30) not null)")
    conn.execute("insert into docinfo values(?,?,?,?,?,?,?,?,?)",(docid1,docname1,sp1,docage1,doccontact1,docemail1,docaddress1,fees1,docms1,))
    conn.commit()
    messagebox.showinfo("Emoloyee Management","Doctor information stored successfully")

def docupdate():
    docid1=docid.get()
    docname1=docname.get()
    sp1=sp.get()
    docage1=docage.get()
    doccontact1=doccontact.get()
    docemail1=docemail.get()
    docaddress1=docaddress.get()
    fees1=fees.get()
    docms1=docms.get()
    conn.execute("update docinfo set docname=?,specialisation=?,age=?,doccontact=?,docemail=?,docaddress=?,fees=?,salary=? where doc_id=?",(docname1,sp1,docage1,doccontact1,docemail1,docaddress1,fees1,docms1,docid1,))
    conn.commit()
    messagebox.showinfo("Employee Management","Doctor Record Updated")

def docdelete():
    docid1=docid.get()
    docname1=docname.get()
    conn.execute("delete from docinfo where doc_id=? and docname=? ",(docid1,docname1,))
    conn.commit()
    messagebox.showinfo("Employee Management","Doctor Record Deleted")

def docsearch():
    docid1=docid.get()
    cursor=conn.execute("select * from docinfo where doc_id=?",(docid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Employee Management","Record Not Found")
    else:
        docid.set(row[0])
        docname.set(row[1])
        sp.set(row[2])
        docage.set(row[3])
        doccontact.set(row[4])
        docemail.set(row[5])
        docaddress.set(row[6])
        fees.set(row[7])
        docms.set(row[8])
        messagebox.showinfo("Employee Management","Doctor Record Searched")


      

def docall():
    cursor=conn.execute("select * from docinfo")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5],",",row[6],",",row[7],",",row[8])
    messagebox.showinfo("Employee Management","Please check all records in output")

l1=Label(dbframe,width=20,bg='powderblue',text='Doctor Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(dbframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Doctor Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=docid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(dbframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Doctor Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=docname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(dbframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Specialisation',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=sp,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(dbframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Age',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=docage,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(dbframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Contact No',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=doccontact,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(dbframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=docemail,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(dbframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Address',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=docaddress,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l9=Label(dbframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Fees',bd=5).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t8=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=fees,bd=5).grid(row=8,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l10=Label(dbframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Monthly Salary',bd=5).grid(row=9,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t9=Entry(dbframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=docms,bd=5).grid(row=9,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=docsave).grid(row=10,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=docupdate).grid(row=10,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=docsearch).grid(row=10,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=docdelete).grid(row=11,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=docall).grid(row=11,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=docreset).grid(row=9,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(dbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous Page',command=docprevious).grid(row=11,column=2,padx=5,pady=5,ipady=5,ipadx=5)

nrsframe=Frame(win)
nrsframe.grid_forget()

def nrsreset():
    nrsid.set("")
    nrsname.set("")
    nrsp.set("")
    nrsage.set("")
    nrscontact.set("")
    nrsemail.set("")
    nrsaddress.set("")
    nrsms.set("")

def nrssave():
    nrsid1=nrsid.get()
    nrsname1=nrsname.get()
    nrsp1=nrsp.get()
    nrsage1=nrsage.get()
    nrscontact1=nrscontact.get()
    nrsemail1=nrsemail.get()
    nrsaddress1=nrsaddress.get()
    nrsms1=nrsms.get()
    conn.execute("create table if not exists nurseinfo(nrs_id char(30) not null,nrsname char(30) not null,specialisation char(30) not null,age char(30) not null,nrscontact char(30) not null,nrsemail char(30) not null, nrsaddress char(30) not null,salary char(30) not null)")
    conn.execute("insert into nurseinfo values(?,?,?,?,?,?,?,?)",(nrsid1,nrsname1,nrsp1,nrsage1,nrscontact1,nrsemail1,nrsaddress1,nrsms1,))
    conn.commit()
    messagebox.showinfo("Emoloyee Management","Nurse information stored successfully")

def nrsupdate():
    nrsid1=nrsid.get()
    nrsname1=nrsname.get()
    nrsp1=nrsp.get()
    nrsage1=nrsage.get()
    nrscontact1=nrscontact.get()
    nrsemail1=nrsemail.get()
    nrsaddress1=nrsaddress.get()
    nrsms1=nrsms.get()
    conn.execute("update nurseinfo set nrsname=?,specialisation=?,age=?,nrscontact=?,nrsemail=?,nrsaddress=?,salary=? where nrs_id=?",(nrsname1,nrsp1,nrsage1,nrscontact1,nrsemail1,nrsaddress1,nrsms1,nrsid1,))
    conn.commit()
    messagebox.showinfo("Employee Management","Nurse Record Updated")

def nrsdelete():
    nrsid1=nrsid.get()
    nrsname1=nrsname.get()
    conn.execute("delete from nurseinfo where nrs_id=? and nrsname=? ",(nrsid1,nrsname1,))
    conn.commit()
    messagebox.showinfo("Employee Management","Doctor Record Deleted")

def nrssearch():
    nrsid1=nrsid.get()
    cursor=conn.execute("select * from nurseinfo where nrs_id=?",(nrsid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Employee Management","Record Not Found")
    else:
        nrsname.set(row[1])
        nrsp.set(row[2])
        nrsage.set(row[3])
        nrscontact.set(row[4])
        nrsemail.set(row[5])
        nrsaddress.set(row[6])
        nrsms.set(row[7])
        messagebox.showinfo("Employee Management","Nurse Record Searched")


def nrsall():
    cursor=conn.execute("select * from nurseinfo")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5],",",row[6],",",row[7])
    messagebox.showinfo("Employee Management","Please check all records in output")

l1=Label(nrsframe,width=20,bg='powderblue',text='Nurse Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Nurse Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Nurse Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Specialisation',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsp,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Age',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsage,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Contact No',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrscontact,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsemail,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Address',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsaddress,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l9=Label(nrsframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Monthly Salary',bd=5).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t8=Entry(nrsframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=nrsms,bd=5).grid(row=8,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=nrssave).grid(row=9,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=nrsupdate).grid(row=9,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=nrssearch).grid(row=9,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=nrsdelete).grid(row=10,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=nrsall).grid(row=10,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=nrsreset).grid(row=8,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(nrsframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous Page',command=nrsprevious).grid(row=10,column=2,padx=5,pady=5,ipady=5,ipadx=5)

wkframe=Frame(win)
wkframe.grid_forget()

def wkreset():
    wkid.set("")
    wkname.set("")
    wk.set("")
    wkage.set("")
    wkcontact.set("")
    wkemail.set("")
    wkaddress.set("")
    wkms.set("")

def wksave():
    wkid1=wkid.get()
    wkname1=wkname.get()
    wk1=wk.get()
    wkage1=wkage.get()
    wkcontact1=wkcontact.get()
    wkemail1=wkemail.get()
    wkaddress1=wkaddress.get()
    wkms1=wkms.get()
    conn.execute("create table if not exists workerinfo(wk_id char(30) not null,wkname char(30) not null,work char(30) not null,age char(30) not null,wkcontact char(30) not null,wkemail char(30) not null, wkaddress char(30) not null,salary char(30) not null)")
    conn.execute("insert into workerinfo values(?,?,?,?,?,?,?,?)",(wkid1,wkname1,wk1,wkage1,wkcontact1,wkemail1,wkaddress1,wkms1,))
    conn.commit()
    messagebox.showinfo("Emoloyee Management","Worker information stored successfully")

def wkupdate():
    wkid1=wkid.get()
    wkname1=wkname.get()
    wk1=wk.get()
    wkage1=wkage.get()
    wkcontact1=wkcontact.get()
    wkemail1=wkemail.get()
    wkaddress1=wkaddress.get()
    wkms1=wkms.get()
    conn.execute("update workerinfo set wkname=?,work=?,age=?,wkcontact=?,wkemail=?,wkaddress=?,salary=? where wk_id=?",(wkname1,wk1,wkage1,wkcontact1,wkemail1,wkaddress1,wkms1,wkid1,))
    conn.commit()
    messagebox.showinfo("Employee Management","Worker Record Updated")

def wkdelete():
    wkid1=wkid.get()
    wkname1=wkname.get()
    conn.execute("delete from workerinfo where wk_id=? and wkname=? ",(wkid1,wkname1,))
    conn.commit()
    messagebox.showinfo("Employee Management","Worker Record Deleted")

def wksearch():
    wkid1=wkid.get()
    cursor=conn.execute("select * from workerinfo where wk_id=?",(wkid1,))
    if cursor is None:
        messagebox.showinfo("Employee Management","Record Not Found")
    else:
       for row in cursor:
            wkname.set(row[1])
            wk.set(row[2])
            wkage.set(row[3])
            wkcontact.set(row[4])
            wkemail.set(row[5])
            wkaddress.set(row[6])
            wkms.set(row[7])
            messagebox.showinfo("Employee Management","Worker Record Searched")


def wkall():
    cursor=conn.execute("select * from workerinfo")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5],",",row[6],",",row[7])
    messagebox.showinfo("Employee Management","Please check all records in output")

l1=Label(wkframe,width=20,bg='powderblue',text='Nurse Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(wkframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Worker Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(wkframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Worker Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(wkframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Work',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wk,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(wkframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Age',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkage,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(wkframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Contact No',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkcontact,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(wkframe,width=10,font=('arial',12,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkemail,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(wkframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Address',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkaddress,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l9=Label(wkframe,width=10,font=('arial',12,'bold'),bg='lavender',fg='black',text='Monthly Salary',bd=5).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t8=Entry(wkframe,font=('arial',12,'bold'),bg='white',fg='black',textvariable=wkms,bd=5).grid(row=8,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=wksave).grid(row=9,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=wkupdate).grid(row=9,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=wksearch).grid(row=9,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=wkdelete).grid(row=10,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=wkall).grid(row=10,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=wkreset).grid(row=8,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(wkframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous Page',command=wkprevious).grid(row=10,column=2,padx=5,pady=5,ipady=5,ipadx=5)



#-----------------------------------------Bill Management----------------------------------------------------------------

billframe=Frame(win)
billframe.grid_forget()

l1=Label(billframe,width=29,bg='bisque',text='Bill management',font=('baskerville old face',30,'bold','underline'),fg='black',justify='center').grid(row=0,column=2,columnspan=4,padx=10,pady=10,ipady=13,ipadx=20)
b1=Button(billframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Lab charges',command=lbshow).grid(row=1,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(billframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Room charges',command=rmshow).grid(row=2,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(billframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Total bill',command=totalshow).grid(row=3,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(billframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Previous Page',command=billprevious).grid(row=4,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)

lbframe=Frame(win)
lbframe.grid_forget()

def psave1():
    pid1=pid.get()
    pname1=pname.get()
    pcontact1=pcontact.get()
    pdiseases1=pdiseases.get()
    mtest1=mtest.get()
    charges1=charges.get()
    conn.execute("create table if not exists lbtest(pid char(30) not null,pname char(30) not null,pcontact char(30) not null,pdisease char(30) not null, mtest char(30) not null, pcharges char(30) not null)")
    conn.execute("insert into lbtest values(?,?,?,?,?,?)",(pid1,pname1,pcontact1,pdiseases1,mtest1,charges1,))
    conn.commit()
    messagebox.showinfo("Lab information","Information stored successfully")

def pupdate1():
    pid1=pid.get()
    pname1=pname.get()
    pcontact1=pcontact.get()
    pdiseases1=pdiseases.get()
    mtest1=mtest.get()
    charges1=charges.get()
    conn.execute("update lbtest set pname=?,pcontact=?,pdisease=?,mtest=?,pcharges=? where pid=?",(pname1,pcontact1,pdiseases1,mtest1,charges1,pid1,))
    conn.commit()
    messagebox.showinfo("Lab information","Information updated")

def psearch1():
    pid1=pid.get()
    cursor=conn.execute("select * from lbtest where pid=?",(pid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Lab information","Information not found")
    else:
        pid.set(row[0])
        pname.set(row[1])
        pcontact.set(row[2])
        pdiseases.set(row[3])
        mtest.set(row[4])
        charges.set(row[5])
        messagebox.showinfo("Lab information","Information searched successfully")

def pdel1():
    pid1=pid.get()
    conn.execute("delete from lbtest where pid=?",(pid1,))
    conn.commit()
    messagebox.showinfo("Lab information","Information deleted")
    
def lbreset():
    pid.set("")
    pname.set("")
    pcontact.set("")
    pdiseases.set("")
    mtest.set("")
    charges.set("")
    
def pall1():
    cursor=conn.execute("select * from lbtest")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5])
    messagebox.showinfo("Lab information","Please check all records in output")

def charges1():
    mtest1=mtest.get()
    if mtest1=="cbc" or mtest1=="CBC":
        charges.set('380')
    elif mtest1=="anemia" or mtest1=="ANEMIA":
        charges.set('1000')
    elif mtest1=="liver"or mtest1=="LIVER":
        charges.set('400')
    elif mtest1=="kidney" or mtest1=="KIDNEY":
        charges.set('200')
    elif mtest1=="lipid" or mtest1=="LIPID":
        charges.set('350')
    elif mtest1=="diabetes" or mtest1=="DIABETES":
        charges.set('100')
    elif mtest1=="bones" or mtest1=="BONES":
        charges.set('700')
    elif mtest1=="malaria" or mtest1=="MALARIA":
        charges.set('120')
    elif mtest1=="dengue" or mtest1=="DENGUE":
        charges.set('250')
    elif mtest1=="full body" or mtest1=="FULL BODY":
        charges.set('1500')
    else:
        messagebox.showinfo("Lab charges","Not Available")
                        
l1=Label(lbframe,width=20,bg='powderblue',text='Patient Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(lbframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(lbframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(lbframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(lbframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(lbframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Disease',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(lbframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pdiseases,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(lbframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Contact No',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(lbframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pcontact,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(lbframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Test name',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(lbframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=mtest,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l8=Label(lbframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Charges',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t7=Entry(lbframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=charges,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=psave1).grid(row=10,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=pupdate1).grid(row=10,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=psearch1).grid(row=10,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=pdel1).grid(row=11,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=pall1).grid(row=11,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=lbreset).grid(row=7,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Charges',command=charges1).grid(row=6,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b8=Button(lbframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous page',command=lbprevious).grid(row=12,column=1,padx=5,pady=5,ipady=5,ipadx=5)

rmframe=Frame(win)
rmframe.grid_forget()

def rmsave1():
    pid1=pid.get()
    pname1=pname.get()
    pcontact1=pcontact.get()
    days1=days.get()
    rmtype1=rmtype.get()
    rmcharges1=rmcharges.get()
    conn.execute("create table if not exists roominfo(pid char(30) not null,pname char(30) not null,pcontact char(30) not null,days char(30) not null,rmtype char(30) not null, rmcharges char(30) not null)")
    conn.execute("insert into roominfo values(?,?,?,?,?,?)",(pid1,pname1,pcontact1,days1,rmtype1,rmcharges1,))
    conn.commit()
    messagebox.showinfo("Room information","Information stored successfully")

def rmupdate1():
    pid1=pid.get()
    pname1=pname.get()
    pcontact1=pcontact.get()
    days1=days.get()
    rmtype1=rmtype.get()
    rmcharges1=rmcharges.get()
    conn.execute("update roominfo set pname=?,pcontact=?,days=?,rmtype=?,rmcharges=? where pid=?",(pname1,pcontact1,days1,rmtype1,rmcharges1,pid1,))
    conn.commit()
    messagebox.showinfo("Room information","Information updated")

def rmsearch1():
    pid1=pid.get()
    cursor=conn.execute("select * from roominfo where pid=?",(pid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Room information","Information not found")
    else:
        pid.set(row[0])
        pname.set(row[1])
        pcontact.set(row[2])
        days.set(row[3])
        rmtype.set(row[4])
        rmcharges.set(row[5])
        messagebox.showinfo("Room information","Information searched successfully")

def rmdel1():
    pid1=pid.get()
    conn.execute("delete from roominfo where pid=?",(pid1,))
    conn.commit()
    messagebox.showinfo("Room information","Information deleted")
    
def rmreset():
    pid.set("")
    pname.set("")
    pcontact.set("")
    days.set("")
    rmtype.set("")
    rmcharges.set("")
    
def rmall1():
    cursor=conn.execute("select * from roominfo")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4],",",row[5])
    messagebox.showinfo("Room information","Please check all records in output")

def rmcharges1():
    rmtype1=rmtype.get()
    try:
        days1=int(days.get())
    except:
        messagebox.showinfo("Room charges","Please Enter valid days")
        return
    if(rmtype1=="general ward" or  rmtype1=="GENERAL WARD"):
        rmcharges.set(1000*days1)
    elif(rmtype1=="private" or  rmtype1=="PRIVATE"):
        rmcharges.set(3000*days1)
    else:
        messagebox.showinfo("Room charges","Not Available")
                        
l1=Label(rmframe,width=20,bg='powderblue',text='Room Information',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(rmframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(rmframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(rmframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(rmframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(rmframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Contact',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(rmframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pcontact,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(rmframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Days',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(rmframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=days,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l6=Label(rmframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Room Type',bd=5).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(rmframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=rmtype,bd=5).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l7=Label(rmframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Room Charges',bd=5).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t6=Entry(rmframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=rmcharges,bd=5).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=rmsave1).grid(row=10,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=rmupdate1).grid(row=10,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=rmsearch1).grid(row=10,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=rmdel1).grid(row=11,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=rmall1).grid(row=11,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=rmreset).grid(row=7,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Charges',command=rmcharges1).grid(row=6,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b8=Button(rmframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous page',command=rmprevious).grid(row=12,column=1,padx=5,pady=5,ipady=5,ipadx=5)

totalframe=Frame(win)
totalframe.grid_forget()

def totalsave():
    pid1=pid.get()
    pname1=pname.get()
    pcontact1=pcontact.get()
    total1=total.get()
    conn.execute("create table if not exists totalcharges(pid char(30) not null,pname char(30) not null,pcontact char(30) not null,total char(30) not null)")
    conn.execute("insert into totalcharges values(?,?,?,?)",(pid1,pname1,pcontact1,total1,))
    conn.commit()
    messagebox.showinfo("Total Bill","Information stored successfully")

def totalupdate():
    pid1=pid.get()
    pname1=pname.get()
    pcontact1=pcontact.get()
    total1=total.get()
    conn.execute("update totalcharges set pname=?,pcontact=?,total=? where pid=?",(pname1,pcontact1,total1,pid1,))
    conn.commit()
    messagebox.showinfo("Total Bill","Information updated")

def totalsearch():
    pid1=pid.get()
    cursor=conn.execute("select * from totalcharges where pid=?",(pid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Total Bill","Information not found")
    else:
        pid.set(row[0])
        pname.set(row[1])
        pcontact.set(row[2])
        total.set(row[3])
        messagebox.showinfo("Total Bill","Information searched successfully")

def totaldel():
    pid1=pid.get()
    conn.execute("delete from totalcharges where pid=?",(pid1,))
    conn.commit()
    messagebox.showinfo("Total Bill","Information deleted")
    
def totalreset():
    pid.set("")
    pname.set("")
    pcontact.set("")
    total.set("")
    
def totalall():
    cursor=conn.execute("select * from totalcharges")
    for row in cursor:
        print(row[0],",",row[1],",",row[2],",",row[3])
    messagebox.showinfo("Total Bill","Please check all records in output")

def totalcharges():
    pid1=pid.get()
    cursor=conn.execute("select pcharges from lbtest where pid=?",(pid1,))
    row1=cursor.fetchone()
    cursor1=conn.execute("select rmcharges from roominfo where pid=?",(pid1,))
    row2=cursor1.fetchone()
    if row1 is None and row2 is None:
        messagebox.showinfo("Total Bill","Lab and room charges not found")
    else:
        cell1=0 if row1 is None else int(row1[0])
        cell2=0 if row2 is None else int(row2[0])
        t1=cell1+cell2
        total.set(t1)

l1=Label(totalframe,width=20,bg='powderblue',text='Total Charges',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
l2=Label(totalframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Patient Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(totalframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(totalframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Patient Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(totalframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pname,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(totalframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Contact',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(totalframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=pcontact,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(totalframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Total',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(totalframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=total,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)


b1=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=totalsave).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=totalupdate).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=totalsearch).grid(row=5,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=totaldel).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=totalall).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=totalreset).grid(row=6,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Total Charges',command=totalcharges).grid(row=4,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b8=Button(totalframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous page',command=totalprevious).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)


#--------------------------------Complaint and suggestion----------------------------------------------------------

csframe=Frame(win)
csframe.grid_forget()

l1=Label(csframe,width=29,bg='bisque',text='Complaint & Suggestion',font=('baskerville old face',30,'bold','underline'),fg='black',justify='center').grid(row=0,column=2,columnspan=4,padx=10,pady=10,ipady=13,ipadx=20)
b1=Button(csframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Complaints',command=compshow).grid(row=1,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(csframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Suggestions',command=sugshow).grid(row=2,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(csframe,width=20,font=('arial',15,'bold'),bg='thistle',fg='purple',bd=5,text='Previous Page',command=csprevious).grid(row=3,column=2,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5)

comframe=Frame(win)
comframe.grid_forget()

def compreset():
    compid.set("")
    name.set("")
    contact.set("")
    email.set("")
    complaint.set("")

def compsave():
    compid1=compid.get()
    name1=name.get()
    contact1=contact.get()
    email1=email.get()
    complaint1=complaint.get()
    conn.execute("create table if not exists complaints(comid int primary key not null,name char(30)not null,contact char(30)not null,emailid char(50)not null,complaint char(100) not null)")
    conn.execute("insert into complaints values(?,?,?,?,?)",(compid1,name1,contact1,email1,complaint1,))
    conn.commit()
    messagebox.showinfo("Hospital Management","Complaint Registered")

def compupdate():
    compid1=compid.get()
    name1=name.get()
    contact1=contact.get()
    email1=email.get()
    complaint1=complaint.get()
    conn.execute("update complaints set name=?,contact=?,emailid=?,complaint=? where comid=?",(name1,contact1,email1,complaint1,compid1,))
    conn.commit()
    messagebox.showinfo("Hospital Management","Complaint Updated")

def compsearch():
    try:
        compid1=int(compid.get())
    except:
        messagebox.showinfo("Hospital Management","Please Enter a valid Complaint Id")
        return
    cursor=conn.execute("select * from complaints where comid=?",(compid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Hospital Management","Complaint Not Found")
    else:
        name.set(row[1])
        contact.set(row[2])
        email.set(row[3])
        complaint.set(row[4])
        messagebox.showinfo("Hospital Management","Complaint searched")

def compall():
    cursor=conn.execute("select * from complaints")
    for row in cursor:
        print(row[0]," ,",row[1]," ,",row[2],", ",row[3],", ",row[4])
    messagebox.showinfo("Hospital Management","Check records in output,")

def compdelete():
    try:
        compid1=int(compid.get())
    except:
        messagebox.showinfo("Hospital Management","Please Enter a valid Complaint Id")
        return
    conn.execute("delete from complaints where comid=?",(compid1,))
    conn.commit()
    messagebox.showinfo("Hospital Management","Record Deleted")

l1=Label(comframe,width=20,bg='powderblue',text='Complaint Section',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5,)

l2=Label(comframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Complaint Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(comframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=compid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(comframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(comframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=name,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(comframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Contact',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(comframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=contact,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(comframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(comframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=email,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)


l6=Label(comframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Complaint',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(comframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=complaint,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)


b1=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=compsave).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=compupdate).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=compsearch).grid(row=6,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=compdelete).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=compall).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=compreset).grid(row=7,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(comframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous page',command=comprevious).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)

sgframe=Frame(win)
sgframe.grid_forget()

def sugreset():
    sugid.set("")
    name.set("")
    contact.set("")
    email.set("")
    suggestion.set("")

def sugsave():
    sugid1=sugid.get()
    name1=name.get()
    contact1=contact.get()
    email1=email.get()
    suggestion1=suggestion.get()
    conn.execute("create table if not exists suggestions(sugid int primary key not null,name char(30)not null,contact char(30)not null,emailid char(50)not null,suggestion char(100) not null)")
    conn.execute("insert into suggestions values(?,?,?,?,?)",(sugid1,name1,contact1,email1,suggestion1,))
    conn.commit()
    messagebox.showinfo("Hospital Management","Suggestion Registered")

def sugupdate():
    sugid1=sugid.get()
    name1=name.get()
    contact1=contact.get()
    email1=email.get()
    suggestion1=suggestion.get()
    conn.execute("update suggestions set name=?,contact=?,emailid=?,suggestion=? where sugid=?",(name1,contact1,email1,suggestion1,sugid1,))
    conn.commit()
    messagebox.showinfo("Hospital Management","Suggestion Updated")

def sugsearch():
    try:
        sugid1=int(sugid.get())
    except:
        messagebox.showinfo("Hospital Management","Please Enter a valid Suggestion Id")
        return
    cursor=conn.execute("select * from suggestions where sugid=?",(sugid1,))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Hospital Management","Suggestion Not Found")
    else:
        name.set(row[1])
        contact.set(row[2])
        email.set(row[3])
        suggestion.set(row[4])
        messagebox.showinfo("Hospital Management","Suggestion searched")

def sugall():
    cursor=conn.execute("select * from suggestions")
    for row in cursor:
        print(row[0]," ,",row[1]," ,",row[2],", ",row[3],", ",row[4])
    messagebox.showinfo("Hospital Management","Check records in output,")

def sugdelete():
    try:
        sugid1=int(sugid.get())
    except:
        messagebox.showinfo("Hospital Management","Please Enter a valid Suggestion Id")
        return
    conn.execute("delete from suggestions where sugid=?",(sugid1,))
    conn.commit()
    messagebox.showinfo("Hospital Management","Record Deleted")

l1=Label(sgframe,width=20,bg='powderblue',text='Suggestion Section',bd='10',font=('baskerville old face',25,'bold','underline'),fg='black',justify='center').grid(row=0,column=1,columnspan=4,padx=5,pady=5,ipady=5,ipadx=5,)

l2=Label(sgframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Suggestion Id',bd=5).grid(row=1,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t1=Entry(sgframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=sugid,bd=5).grid(row=1,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l3=Label(sgframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Name',bd=5).grid(row=2,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t2=Entry(sgframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=name,bd=5).grid(row=2,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l4=Label(sgframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Contact',bd=5).grid(row=3,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t3=Entry(sgframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=contact,bd=5).grid(row=3,column=1,padx=5,pady=5,ipady=5,ipadx=5)

l5=Label(sgframe,width=10,font=('arial',15,'bold'),bg='gainsboro',fg='black',text='Email Id',bd=5).grid(row=4,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t4=Entry(sgframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=email,bd=5).grid(row=4,column=1,padx=5,pady=5,ipady=5,ipadx=5)


l6=Label(sgframe,width=10,font=('arial',15,'bold'),bg='lavender',fg='black',text='Suggestion',bd=5).grid(row=5,column=0,padx=5,pady=5,ipady=5,ipadx=5)
t5=Entry(sgframe,font=('arial',15,'bold'),bg='white',fg='black',textvariable=suggestion,bd=5).grid(row=5,column=1,padx=5,pady=5,ipady=5,ipadx=5)

b1=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Save',command=sugsave).grid(row=6,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b2=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Update',command=sugupdate).grid(row=6,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b3=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Search',command=sugsearch).grid(row=6,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b4=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Delete',command=sugdelete).grid(row=7,column=0,padx=5,pady=5,ipady=5,ipadx=5)
b5=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Show All',command=sugall).grid(row=7,column=1,padx=5,pady=5,ipady=5,ipadx=5)
b6=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Reset',command=sugreset).grid(row=7,column=2,padx=5,pady=5,ipady=5,ipadx=5)
b7=Button(sgframe,width=10,bd=5,font=('arial',10,'bold'),bg='royalblue',fg='white',text='Previous page',command=sgprevious).grid(row=8,column=0,padx=5,pady=5,ipady=5,ipadx=5)

win.mainloop()