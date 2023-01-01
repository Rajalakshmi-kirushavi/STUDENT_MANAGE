from tkinter import *
import mysql.connector
from mysql import *


def connection():
    # database Connection Statements

    global conn
    try:
        conn = mysql.connector.connect(host='localhost', database='testdb1', user='root', password='Adm1n5p3c@')
        connection.cursor()
    except:
        print("cannot connect to the database")
    return conn


def verifier(t1=None):
    # Checks all the Input Fields gets the data

    a = b = c = d = e = f = g = h = i = 0
    if not student_name.get():
        t1.insert(END, "<>Student name is required<>\n")
        a = 1
    if not roll_no.get():
        t1.insert(END, "<>Roll no is required<>\n")
        b = 1
    if not branch.get():
        t1.insert(END, "<>Branch is required<>\n")
        c = 1
    if not phone.get():
        t1.insert(END, "<>Phone number is required<>\n")
        d = 1
    if not father.get():
        t1.insert(END, "<>Father name is required<>\n")
        e = 1
    if not address.get():
        t1.insert(END, "<>Address is Required<>\n")
        f = 1
    if not city.get():
        t1.insert(END, "<>City is Required<>")
        g = 1
    if not state.get():
        t1.insert(END, "<>State is Required<>")
        h = 1
    if not pincode.get():
        t1.insert(END, "<>Pincode is Required")
        i = 1
    if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1 or g == 1 or h == 1 or i == 1:
        return 1
    else:
        return 0


def add_student():
    # This Function checks the input fields and add the student Details into the Database

    # ret = verifier()
    # if ret == 0:
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='testdb1',
                                       user='root',
                                       password='Adm1n5p3c@')
        cur = conn.cursor()
        # cur.execute(
        #     "CREATE TABLE IF NOT EXISTS STUDENT_DETAIL(NAME TEXT,ROLL_NO INTEGER,DEPARTMENT TEXT,FATHER TEXT,"
        #     "ADDRESS TEXT,CITY TEXT,STATE TEXT,PINCODE TEXT,MOBILE_NUM TEXT)")
        insert_query = """INSERT INTO student_detail(NAME,ROLL_NO,DEPARTMENT,FATHER,ADDRESS, CITY,STATE,PINCODE,
                        MOBILE_NUM) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) """
        insert_values = (student_name.get(), roll_no.get(), branch.get(), father.get(), address.get(), city.get(),
                         state.get(), pincode.get(), phone.get())

        cur.execute(insert_query, insert_values)
        conn.commit()
        print("Data Inserted")
        t1.insert(END, "ADDED SUCCESSFULLY\n")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    #

    finally:
        if conn.is_connected():
            cur.close()
            conn.close()


def view_student():
    # This function is to view the student details in  the text area

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='testdb1',
                                       user='root',
                                       password='Adm1n5p3c@')
        cur = conn.cursor()
        view_data_query = """SELECT * FROM student_detail"""
        cur.execute(view_data_query)
        data = cur.fetchall()
        
        for i in data:
            # t1.state = "normal"

            t1.insert(END, (str(i) + "\n"))
            print(str(i))
    except mysql.connector.Error as error:
        print("Failed to fetch data from MySQL table {}".format(error))
    #
    finally:
        if conn.is_connected():
            cur.close()
            conn.close()
            print("MySQL connection is closed")


def delete_student():
    # This function is used to delete the particular Student Details

    # ret = verifier()
    # if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM student_detail WHERE ROLL_NO=%s", (int(roll_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END, "SUCCESSFULLY DELETED THE USER\n")


def update_student():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE STUDENT_DETAIL SET NAME=%s,ROLL_NO=%s,DEPARTMENT=%s,FATHER=%s,ADDRESS=%s,CITY=%s,STATE=%s,"
                    "PINCODE=%s,MOBILE_NUM=%s where ROLL_NO=%s", (
                        student_name.get(), int(roll_no.get()), branch.get(), father.get(), address.get(), city.get(),
                        state.get(), pincode.get(), phone.get(), roll_no.get()))
        conn.commit()
        conn.close()
        t1.insert(END, "UPDATED SUCCESSFULLY\n")


def close():
    root.quit()


if __name__ == "__main__":
    root = Tk()
    root.title("Student Management System")

    student_name = StringVar()
    roll_no = StringVar()
    branch = StringVar()
    phone = StringVar()
    father = StringVar()
    address = StringVar()
    city = StringVar()
    state = StringVar()
    pincode = StringVar()

    label1 = Label(root, text="Student name:")
    label1.grid(row=0, column=0)

    label2 = Label(root, text="Roll no:")
    label2.grid(row=1, column=0)

    label3 = Label(root, text="Department:")
    label3.grid(row=2, column=0)

    label4 = Label(root, text="Father's Name:")
    label4.grid(row=3, column=0)

    label5 = Label(root, text="Address:")
    label5.grid(row=4, column=0)

    label6 = Label(root, text="City:")
    label6.grid(row=5, column=0)

    label7 = Label(root, text="State:")
    label7.grid(row=6, column=0)

    label8 = Label(root, text="Pincode:")
    label8.grid(row=7, column=0)

    label9 = Label(root, text="Mobile Number:")
    label9.grid(row=8, column=0)

    e1 = Entry(root, textvariable=student_name)
    e1.grid(row=0, column=1)

    e2 = Entry(root, textvariable=roll_no)
    e2.grid(row=1, column=1)

    e3 = Entry(root, textvariable=branch)
    e3.grid(row=2, column=1)

    e4 = Entry(root, textvariable=father)
    e4.grid(row=3, column=1)

    e5 = Entry(root, textvariable=address)
    e5.grid(row=4, column=1)

    e6 = Entry(root, textvariable=city)
    e6.grid(row=5, column=1)

    e7 = Entry(root, textvariable=state)
    e7.grid(row=6, column=1)

    e8 = Entry(root, textvariable=pincode)
    e8.grid(row=7, column=1)

    e9 = Entry(root, textvariable=phone)
    e9.grid(row=8, column=1)

    t1 = Text(root, width=50, height=20)
    t1.grid(row=10, columnspan=2)

    b1 = Button(root, text="ADD STUDENT", command=add_student, width=30)
    b1.grid(row=11, column=0)

    b2 = Button(root, text="VIEW ALL STUDENTS", command=view_student, width=30)
    b2.grid(row=12, column=0)

    b3 = Button(root, text="DELETE STUDENT", command=delete_student, width=30)
    b3.grid(row=13, column=0)

    b4 = Button(root, text="UPDATE INFO", command=update_student, width=30)
    b4.grid(row=14, column=0)

    b5 = Button(root, text="CLOSE", command=close, width=30)
    b5.grid(row=15, column=0)

    root.mainloop()
