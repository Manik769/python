from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database_student
import database_course
from PIL import Image,ImageTk
def main():
    window=tk.Tk()
    app=loginpage(window)
    window.mainloop()
class loginpage():
    def __init__(self,window):
        self.window=window
        self.window.title("Login Form")
        self.window.geometry("300x300")
        self.window.config(bg="dark blue")
        self.window.resizable(False,False)
        username = StringVar()
        password = StringVar()
        Label(window,width="300", text="Please enter details below", bg="orange",fg="white").pack()
        Label(window,text="Username * ").place(x=20,y=40)
        Entry(window,textvariable=username).place(x=120,y=42)
        Label(window,text="Password * ").place(x=20,y=80)
        Entry(window,textvariable=password,show="*").place(x=120,y=82)
        def login():
            uname=username.get()
            pwd=password.get()
            if uname=="" or pwd=="":
                messagebox.showinfo("fill the details please")
            elif uname=="manik" and pwd=="123":
                messagebox.showinfo("login","login successful")
                self.new_window=Toplevel(window)
                self.app=window2(self.new_window)
            else:
                messagebox.showinfo("wrong","wrong username or password")
        self.button=Button(window,text="login", width=10, height=1, bg="light pink",command=login).place(x=120,y=150)
class window2:
    def __init__(self,window):
        def open_page():
            self.new_window=Toplevel(window)
            self.app=window3(self.new_window)
        self.window=window
        self.window.geometry("2000x1200")
        self.window.title("student mangement")
        self.window.config(bg="white")
        def open_page1():
            self.new_window=Toplevel(window)
            self.app=window4(self.new_window)
        def logout_1():
            window.destroy()
        img1=Image.open(r"C:\\Users\\USER\\Downloads\\th (15).jpg")
        self.photo1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.window,image=self.photo1)
        f_lbl1.place(x=5,y=-15)
            
        self.text=Label(window,text="STUDENT MANAGEMENT SYSTEM",font=("Calibri",35, "bold"),bg="light pink",bd=6, relief=GROOVE,width=50).place(x=40,y=-5)
        self.lframe=LabelFrame(window,text="Menu",bg="light blue",bd=5,relief=GROOVE,width=600,height=100,font=("Calibri",15, "bold")).place(x=350,y=400)
        self.submitbutton=Button(window,text="Courses",width=12,command=open_page, font=("Calibri", 10, "italic"), fg="black", bg="blue", relief=RIDGE, bd=10).place(x=400,y=430)
        self.studentbutton=Button(window,text="Student",width=12,command=open_page1,font=("Calibri", 10, "italic"), fg="black", bg="blue", relief=RIDGE, bd=10).place(x=600,y=430)
        '''self.resultsbutton=Button(window,text="Results",width=12,font=("Calibri", 10, "italic"), fg="black", bg="blue", relief=RIDGE, bd=10).place(x=550,y=200)
        self.resultsbutton=Button(window,text="View the Results",width=12,font=("Calibri", 10, "italic"), fg="black", bg="blue", relief=RIDGE, bd=10).place(x=750,y=200)'''
        self.resultsbutton=Button(window,text="Logout",command=logout_1,width=12,font=("Calibri", 10, "italic"), fg="black", bg="blue", relief=RIDGE, bd=10).place(x=800,y=430)
        
         

class window3:
    def __init__(self,window):
        def view():
            tree.delete(*tree.get_children())
            for data in database_student.view():
                tree.insert('','end',values=(data))
                tree.bind("<Double-1>",get_selected_data)
        def search():
             tree.delete(*tree.get_children())
             for data in database_student.search(coursename=coursename.get(),duration=duration.get(),charges=charges.get(),description=description.get()):
                tree.insert('','end',values=(data))
        def add():
            database_student.add(coursename.get(),duration.get(),charges.get(),description.get())
            messagebox.showinfo("sumbit","Sumbited successfully")
            tree.delete(*tree.get_children())
            tree.insert('','end',values=(coursename.get(),duration.get(),charges.get(),description.get()))
        def get_selected_data():
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            coursename.set(selecteditem[1])
            duration.set(selecteditem[2])
            charges.set(selecteditem[3])
            description.set(selecteditem[4])
            
        def update():
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            database_student.update( selecteditem[0],coursename.get(),duration.get(),charges.get(),description.get())
            messagebox.showinfo("update","updates successfully")
            view()
        def delete():
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            database_student.delete( selecteditem[0])
            messagebox.showinfo("delete","deleted successfully")
            view()
        def clear():
            tree.delete(*tree.get_children())
            coursename.set("")
            duration.set("")
            charges.set("")
            description.set("")
            view()
    

        self.window=window
        self.window.geometry("2000x1200")
        self.window.title("student mangement")
        self.window.config(bg="light blue")
        self.text=Label(window,text="Course Management System",font=("Calibri",35, "bold"),bg="light pink",bd=6, relief=GROOVE,width=50).place(x=40,y=40)
        self.frame=Frame(window,bg="white",bd=6, relief=GROOVE,width=500,height=440).place(x=80,y=150)
        self.lframe=LabelFrame(window,text="Student Information",bg="light blue",bd=5,relief=GROOVE,width=450,height=400,font=("Calibri",15, "bold")).place(x=100,y=170)
        self.ltabletsname=Label(window,text="Course name",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=220)
        self.ldose =Label(window,text="Duration",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=280)
        self.ltabletsno=Label(window,text="Charges",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=340)
        self.ltabletsno=Label(window,text="Description",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=400)
        coursename=StringVar()
        self.Entrytabletsname=Entry(window,textvariable=coursename,font=("Calibri", 14, "italic")).place(x=290,y=220)                                                                                                                                
        duration=StringVar()
        self.Entrydose=Entry(window,textvariable=duration,font=("Calibri", 14, "italic")).place(x=290,y=280)
        charges=IntVar()
        self.Entrytabletsno=Entry(window,textvariable=charges,font=("Calibri", 14, "italic")).place(x=290,y=340)
        description=StringVar()
        self.Entrydescription=Entry(window,textvariable=description,font=("Calibri", 14, "italic")).place(x=290,y=400)
        self.submitbutton=Button(window,text="Add",width=12,command=add,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=100,y=600)
        self.updatebutton=Button(window,text="Update",width=12,command=update,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=300,y=600)
        self.deletebutton=Button(window,text="Delete",width=12,command=delete,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=500,y=600)
        self.searchbutton=Button(window,text="Search",width=12,command=search,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=700,y=600)
        self.viewbutton=Button(window,text="View",width=12,command=view, font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=900,y=600)
        self.clearhbutton=Button(window,text="Clear",width=12,command=clear,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=1100,y=600)
        
        def logout():
            window.destroy()
        self.logouthbutton=Button(window,text="logout",width=12,command=logout,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=1250,y=600)

        scrollbarx=Scrollbar(window,orient=HORIZONTAL)
        scrollbary=Scrollbar(window,orient=VERTICAL)
        tree=ttk.Treeview(window,columns=("id","coursename","duration","charges","descripton"),show="headings",selectmode="extended",xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
        scrollbary.config(command=tree.yview)
        scrollbary.place(x=1230,y=250)
        scrollbarx.config(command=tree.xview)
        scrollbarx.place(x=800,y=400)
        tree.heading("id",text="id")
        tree.heading("coursename",text="Course name")
        tree.heading("duration",text="Duration")
        tree.heading("charges",text="Charges")
        tree.heading("descripton",text="Descripton")
        tree.column("id",width=0)
        tree.column("coursename",width=150)
        tree.column("duration",width=100)
        tree.column("charges",width=120)
        tree.column("descripton",width=140)
        tree.place(x=600,y=170)
class window4():
    def __init__(self,window):
        def view():
            tree.delete(*tree.get_children())
            for data in database_course.view():
                tree.insert('','end',values=(data))
                tree.bind("<Double-1>",get_selected_data)
        def search():
             tree.delete(*tree.get_children())
             for data in database_course.search(rollno=rollno.get(),name=name.get(),gender=gender.get(),state=state.get(),course=course.get()):
                tree.insert('','end',values=(data))
        def add():
            database_course.add(rollno.get(),name.get(),gender.get(),state.get(),course.get())
            messagebox.showinfo("sumbited","Sumbited successfully")
            tree.delete(*tree.get_children())
            tree.insert('','end',values=(rollno.get(),name.get(),gender.get(),state.get(),course.get()))
        def get_selected_data():
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            rollno.set(selecteditem[1])
            name.set(selecteditem[2])
            gender.set(selecteditem[3])
            state.set(selecteditem[4])
            course.set(selecteditem[5])
        def update():
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            database_course.update( selecteditem[0],rollno.get(),name.get(),gender.get(),state.get(),course.get())
            messagebox.showinfo("updated","updates successfully")
            view()
        def delete():
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents['values']
            database_course.delete( selecteditem[0])
            messagebox.showinfo("deleted","deleted successfully")
            view()
        def clear():
            tree.delete(*tree.get_children())
            rollno.set("")
            name.set("")
            gender.set("")
            state.set("")
            course.set("")
            view()
        def logout():
            window.destroy()
        self.logouthbutton=Button(window,text="logout",width=12,command=logout,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=1250,y=600)
    
        self.window=window
        self.window.geometry("2000x1200")
        self.window.title("student mangement")
        self.window.config(bg="light blue")
        self.text=Label(window,text="Student Management System",font=("Calibri",35, "bold"),bg="light pink",bd=6, relief=GROOVE,width=50).place(x=40,y=40)
        self.frame=Frame(window,bg="white",bd=6, relief=GROOVE,width=500,height=440).place(x=80,y=150)
        self.lframe=LabelFrame(window,text="Student Information",bg="light blue",bd=5,relief=GROOVE,width=450,height=400,font=("Calibri",15, "bold")).place(x=100,y=170)
        self.lrollno=Label(window,text="Roll No",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=220)
        self.lname=Label(window,text="Name",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=280)
        self.lgender=Label(window,text="Gender",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=340)
        self.lstate=Label(window,text="State",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=400)
        self.lcourse=Label(window,text="Course",font=("Calibri", 14, "bold"), fg="black", bg="white").place(x=125,y=480)
        rollno=IntVar()
        self.Entryrollno=Entry(window,textvariable=rollno,font=("Calibri", 14, "italic")).place(x=290,y=220)                                                                                                                                
        name=StringVar()
        self.Entrname=Entry(window,textvariable=name,font=("Calibri", 14, "italic")).place(x=290,y=280)
        gender=StringVar()
        self.Entrygender=Entry(window,textvariable=gender,font=("Calibri", 14, "italic")).place(x=290,y=340)
        state=StringVar()
        self.Entrystate=Entry(window,textvariable=state,font=("Calibri", 14, "italic")).place(x=290,y=400)
        course=StringVar()
        self.Entrycourse=Entry(window,textvariable=course,font=("Calibri", 14, "italic")).place(x=290,y=480)
        self.submitbutton=Button(window,text="Add",width=12,command=add, font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=100,y=600)
        self.updatebutton=Button(window,text="Update",width=12,command=update ,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=300,y=600)
        self.deletebutton=Button(window,text="Delete",width=12,command=delete, font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=500,y=600)
        self.searchbutton=Button(window,text="Search",width=12,command=search, font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=700,y=600)
        self.viewbutton=Button(window,text="View",width=12,command=view, font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=900,y=600)
        self.clearhbutton=Button(window,text="Clear",width=12,command=clear,font=("Calibri", 10, "italic"), fg="black", bg="green", relief=RIDGE, bd=10).place(x=1100,y=600)

        scrollbarx=Scrollbar(window,orient=HORIZONTAL)
        scrollbary=Scrollbar(window,orient=VERTICAL)
        tree=ttk.Treeview(window,columns=("rollno","name","gender","state","course"),show="headings",selectmode="extended",xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
        scrollbary.config(command=tree.yview)
        scrollbary.place(x=1200,y=250)
        scrollbarx.config(command=tree.xview)
        scrollbarx.place(x=800,y=400)
        tree.heading("rollno",text="Roll no")
        tree.heading("name",text="Name")
        tree.heading("gender",text="Gender")
        tree.heading("state",text="State")
        tree.heading("course",text="Course")
        tree.column("rollno",width=100)
        tree.column("name",width=100)
        tree.column("gender",width=120)
        tree.column("state",width=100)
        tree.column("course",width=100)
        tree.place(x=600,y=170)

if __name__ == "__main__":
    main()        
