
import mysql.connector as sql
password= input("Database Password : ")
con=sql.connect(host="localhost", user="root", passwd=password, database="myschool")

connect = con.cursor()
connect.execute("Show Databases")
dl = connect.fetchall()
dl2= []
for i in dl:
    dl2.append(i[0])
if 'myschool' in dl2:
    sql1 = "Use myschool"
    connect.execute(sql1)
else:
    sql2 = "Create Database myschool"
    connect.execute(sql2)
    sql3 = "Use myschool"
    connect.execute(sql3)
    sql4 = '''create table Student(Name varchar(50),Enrollment_No varchar int,Class varchar(10),Roll_No int,Address int,phone int)'''
    connect.execute(sql4)
    sql5 = '''create table Fees(Name varchar(20),Enrollment_No bigint,Class varchar(10),Fees bigint,Phone bigint, Date date)'''
    connect.execute(sql5)
    sql6 = '''create table Teacher(Name varchar(30),Id bigint, Work varchar(20),salary bigint)'''
    connect.execute(sql6)
    con.commit()

def Add_Student():
    name =input("Enter the Student Name : ")
    enr = input("Enter the Enrollment No : ")
    cla = input("Enter the Class : ")
    roll_no = input("Enter the Roll No : ")
    add = input("Enter the Permanent Address : ")
    pho = input("Enter the Phone No : ")
    data = (name, enr, cla, roll_no, add, pho)
    sql = 'insert into Student values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully")

def Pay_Fees():
    name = input("Enter the Student Name : ")
    enr = input("Enter the Enrollment No : ")
    cls = input("Enter the Class : ")
    fees = input("Enter the Fees : ")
    phone = input("Enter the Phone No : ")
    date = input("Enter the Date : ")
    data = (name, enr, cls, fees, phone, date)
    sql = 'insert into Fees values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully")

def Add_Teacher():
    name = input("Enter the Teacher Name : ")
    Id = input("Enter the Teacher Id :  ")
    work = input("Enter the Teacher Work/Subject : ")
    salary = input("Enter the Teacher Salary : ")
    data =(name, Id, work, salary)
    sql = 'insert into Teacher values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute (sql, data)
    con.commit()
    print("Data Inserted Successfully")


def Del_Student():
    cla = input("Enter the Class : ")
    roll_no = input("Enter the Roll No : ")
    data =(cla, roll_no)
    sql = 'delete from Student where class = %s and roll_no = %s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit ()
    print ("Data Updated Successfully")

def Del_Teacher():
    Id = input("Enter Teacher Id :  ")
    work = input("Enter the Teacher Work/Subject : ")
    data =(Id, work)
    sql = 'delete from Teacher where Id = %s and work = %s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit ()
    print ("Data Updated Successfully")

def Dis_Student():
    cls = input("Enter the Class : ")
    sql = 'select * from Student'
    c = con.cursor()
    c.execute(sql)
    display = c.fetchall()
    for i in display:
        if i[2] == cls:
            print("\nStudent Details :- ")
            print("-----------------------")
            print("Name :", i[0])
            print("Enrollment No : ", i[1])
            print("Class : ", i[2])
            print("Roll No : ", i[3])
            print("Address : ", i[4])
            print("Phone : ", i[5])
            print("------------------------")
        else:
            print("Data Not Found !")

def Dis_Fees():
    cls = input("Enter the Class : ")
    date = input("Enter the Date : ")
    sql = 'select * from Fees'
    c = con.cursor()
    c.execute (sql)
    display = c.fetchall()
    for i in display :
        if i[2] == cls or i[5] == date :
            print("\nStudent Fees Details  :- ")
            print("-----------------------")
            print("Name :", i[0])
            print("Enrollment No : ", i[1])
            print("Class : ", i[2])
            print("Fess : ", i[3])
            print("Date : ", i[5])
            print( "------------------------")
        else :
            print ("Data Not Found !")


def Dis_Teacher():
    work = input("Enter Teacher Work/Subject :  ")
    sql = 'select * from Teacher'
    c = con.cursor()
    c.execute(sql)
    display = c.fetchall()
    for i in display:
        if i[2] == work:
            print ("\nTeacher Details :- " )
            print("---------------------")
            print("Teacher Name :", i[0])
            print("Id No :", i[1])
            print("Work : ", i[2])
            print("salary : ", i[3])
            print("----------------------")
        else:
            if work is None:
                print("Data Not Found !")




# PROJECT WORKING OPTIONS
while True:
    print("\n")
    print("\t\t\t\t\t\t\t\t\t ----------->>>>>>>>> WELCOME <<<<<<<<<--------------")
    print("\t\t\t\t\t\t\t\t\t >>>>>>>> Delhi International School [D.I.S] <<<<<<<<")
    print("\t\t\t\t\t\t\t\t\t ...................................................")
    print("\t\t\t\t\t\t\t\t\t 1. Add Student                  5. Display Student ")
    print("\t\t\t\t\t\t\t\t\t 2. Add Teachers                 6. Display Teachers")
    print("\t\t\t\t\t\t\t\t\t 3. Add Fess                     7. Display Fees    ")
    print("\t\t\t\t\t\t\t\t\t 4. Delete Student               8. Delete Teacher  ")
    print("\t\t\t\t\t\t\t\t\t                     9. Quit                        ")
    print("\t\t\t\t\t\t\t\t\t ....................................................")
    choice = int (input ("Select Option : "))
    if choice == 1:
        Add_Student()
    elif choice == 2:
        Add_Teacher()
    elif choice == 3:
        Pay_Fees()
    elif choice == 4:
        Del_Student()
    elif choice == 5:
        Dis_Student()
    elif choice == 6:
        Dis_Teacher()
    elif choice == 7:
        Dis_Fees()
    elif choice == 8:
        Del_Teacher()
    elif choice == 9:
        break
    else:
        print("Incorrect Choice....")
        print("Enter Again.....")

