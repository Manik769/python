import sqlite3
def create():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS tablestudent(id INTEGER PRIMARY KEY,coursename TEXT,duration TEXT,charges INTEGER,description TEXT)")
    con.close()
def view():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * from tablestudent")
    rows=cur.fetchall()
    con.close()
    return rows
def search(coursename="",duration ="",charges="",description=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * from tablestudent  WHERE coursename=? OR duration=? OR charges=? OR description=? ",(coursename,duration,charges,description))
    rows=cur.fetchall()
    con.close()
    return rows
def add(coursename,duration,charges,description):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("INSERT INTO tablestudent VALUES(NULL,?,?,?,?)",(coursename,duration,charges,description))
    con.commit()
    con.close()
def update(id,coursename,duration,charges,description):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE tablestudent SET coursename=?,duration=?,charges=?,description=? WHERE id=?",(coursename,duration,charges,description,id))
    con.commit()
    con.close()
def delete(id):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE  from tablestudent WHERE id=?",(id,))
    con.commit()
    con.close()
create()


    
    
