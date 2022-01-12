import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',
                            password='MANAGER',db='db2')
cur=con.cursor()


#main menu
def mainmenu():
    print("_"*50,'\n\n'
          "1.add new records\n"
          "2.show all records\n"
          "3.search a record\n"
          "4.update a record\n"
          "5.delete a record\n"
          "6.exit")
    print("_"*50)
    
    



def createtable():
    cur.execute("create table hospital(serial_no varchar(10) primary key,name char(20),gender char(1),age int,address varchar(100),city char(20),blood varchar(5),casuality char(30),doctor char(20),contact varchar(11),email varchar(25))")
    print("table created successfully")
    
def newrecord():
    while True:
        serial=input("enter serial no.:")
        name=input("enter name:")
        gender=input("enter gender(M/F):")
        age=int(input("enter age:"))
        address=input("enter address:")
        city=input("enter city:")
        blood=input("enter blood group:")
        casuality=input("enter (disease/injury) suffered by patient:")
        doctor=input("enter doctor name undertaking the patient:")
        contact=int(input("enter contact number:"))
        email=input("enter e-mail:")
        val=[serial,name,gender,age,address,city,blood,casuality,doctor,contact,email]
        cmd="insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(cmd,val)
        con.commit()
        print()
        x=input("do you want to add more records(Y/N):")
        if x=="N" or x=="n":
            print("\ndata saved successfully")
            break
        
    

def records():
    rec="select * from hospital"
    cur.execute(rec)
    m=cur.fetchall()
    c=1
    for i in m:
        print(c,end="=>")
        print(i,end="\n\n")
        c=c+1
    
def searchmenu():
    print("<=SEARCH BY=>\n"
          "a.name\n"
          "b.serial number\n"
          "c.blood group\n"
          "d.age\n"
          "e.gender\n"
          "f.city\n"
          "g.doctor\n"
          "h.contact number\n"
          "i.e-mail\n"
          "j.disease/injury")
    x=input("enter your option:")
    try:
            
        if x=="a" or x=="A":
            nm=input("enter name:")
            run="select * from hospital where name='%s'"%nm
        elif x=="b" or x=="B":                   
            serial=input("enter serial number:")
            run="select * from hospital where serial_no='%s'"%serial
        elif x=="c" or x=="C":
            bld=input("enter blood group:")
            run="select * from hospital where blood='%s'"%bld
        elif x=="d" or x=="D":
            age1=input("enter age:")
            run="select * from hospital where age='%s'"%age1
        elif x=="e" or x=="E":
            gen=input("enter gender(M/F):")
            run="select * from hospital where gender='%s'"%gen
        elif x=="f" or x=="F":
            c=input("enter city:")
            run="select * from hospital where city='%s'"%c
        elif x=="g" or x=="G":
            doc=input("enter doctor name:")
            run="select * from hospital where doctor='%s'"%doc
        elif x=="h" or x=="H":
            num=input("enter contact no.:")
            run="select * from hospital where contact='%s'"%num
        elif x=="i" or x=="I":
            mail=input("enter e-mail:")
            run="select * from hospital where email='%s'"%mail
        elif x=="j" or x=="J":               # check it later
            casuality=input("enter (disease/injury):")
            run="select * from hospital where casuality='%s'"%casuality
        
            
        cur.execute(run)
        q=cur.fetchall()
        if q==[]:
            print("\nno match found")
        x=1
        for i in q:
            print(x,end="=>")
            print(i,end="\n\n")
            x=x+1
        
    except:
        print("\nwrong entry\ntry again")

def update():
    while True:
        
         try:
             se=input("enter serial no.:")
             R="select * from hospital where serial_no='%s'"%se
             cur.execute(R)
             q=cur.fetchall()
             if q==[]:
                 print("no match found")
                 break
             print("<=what you want to change=>\n"
                   "a.name\n"
                   "b.disease/injury\n"
                   "c.blood group\n"
                   "d.age\n"
                   "e.gender\n"
                   "f.city\n"
                   "g.doctor\n"
                   "h.contact number\n"
                   "i.e-mail")
             x=input("enter your option:")

             if x=="a" or x=="A" :
                 nm=input("enter name:")
                 run="update hospital set name='%s' where serial_no='%s'"%(nm,se)
             elif x=="b" or x=="B":              
                 casuality=input("enter (disease/injury):")
                 run="update hospital set casuality='%s' where serial_no='%s'"%(casuality,se)
             elif x=="c" or x=="C":
                 bld=input("enter blood group:")
                 run="update hospital set blood='%s' where serial_no='%s'"%(bld,se)
             elif x=="d" or x=="D":
                 age1=input("enter age:")
                 run="update hospital set age='%s' where serial_no='%s'"%(age1,se)
             elif x=="e" or x=="E":
                 gen=input("enter gender(M/F):")
                 run="update hospital set gender='%s' where serial_no='%s'"%(gen,se)
             elif x=="f" or x=="F":
                 c=input("enter city:")
                 run="update hospital set city='%s' where serial_no='%s'"%(c,se)
             elif x=="g" or x=="G":
                 doc=input("enter doctor name:")
                 run="update hospital set doctor='%s' where serial_no='%s'"%(doc,se)
             elif x=="h" or x=="H":
                 num=input("enter contact no.:")
                 run="update hospital set contact='%s' where serial_no='%s'"%(num,se)
             elif x=="i" or x=="I":
                 mail=input("enter e-mail:")
                 run="update hospital set email='%s' where serial_no='%s'"%(mail,se)
             cur.execute(run)
             con.commit()
             
             op=input("do you want to change more records(Y/N):")
             
             if op=="N" or op=="n":
                 print("\ndata updated successfully")
                 break
         except:
            print("\nwrong entry try again\n")

def delete():
    try:
        de=input("enter serial number:")
        x="select * from hospital where serial_no='%s'"%de
        cur.execute(x)
        opt=cur.fetchall()
        if opt!=[]:
            run="delete from hospital where serial_no='%s'"%de
            cur.execute(run)
            con.commit()
            print("\ndata deleted successfully")
        else:
            print("\ndata doesn't exist")
    except:
        print("\nno such serial no. exist")




createtable()
while True:
    try:
        mainmenu()
        ans=int(input("enter your choice: "))
        if ans==1:
            newrecord()
        elif ans==2:
            records()
        elif ans==3:
            searchmenu()
        elif ans==4:
            update()
        elif ans==5:
            delete()
        
        elif ans==6:
            print("<=thanks for using=>")
            break
        else:
            print("\nyou have entered invalid option"
                  "enter valid option")

    except:
         print("\nyou have entered invalid option\n"
                  "enter valid option")
