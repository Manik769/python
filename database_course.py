import sqlite3
def create():
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS tablecourse(id INTEGER PRIMARY KEY , rollno INTEGER UNIQUE,name TEXT,gender TEXT,state TEXT,course TEXT)")
    con.close()
def view():
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    cur.execute("SELECT * from tablecourse")
    rows=cur.fetchall()
    con.close()
    return rows
def search(rollno="",name="",gender="",state="",course=""):
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    cur.execute("SELECT * from tablecourse  WHERE  rollno=? OR name=? OR gender=? OR state=? OR course=? ",(rollno,name,gender,state,course))
    rows=cur.fetchall()
    con.close()
    return rows
def add(rollno,name,gender,state,course):
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    cur.execute("INSERT INTO tablecourse VALUES(NULL,?,?,?,?,?)",(rollno,name,gender,state,course))
    con.commit()
    con.close()
def update(id,rollno,name,gender,state,course):
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    cur.execute("UPDATE tablecourse SET rollno=?,name=?,gender=?,state=?,course=? WHERE id=?",(rollno,name,gender,state,course,id))
    con.commit()
    con.close()
def delete(id):
    con=sqlite3.connect("student1.db")
    cur=con.cursor()
    cur.execute("DELETE  from tablecourse WHERE id=?",(id,))
    con.commit()
    con.close()
create()


    
    
