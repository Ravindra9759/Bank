from prettytable import PrettyTable
import mysql.connector
from datetime import date
dt=date.today()

con=mysql.connector.connect(host='localhost',user='root',password='',database='mydb')
cur=con.cursor()
print("Press 0 to Check Your Info")
print("Press 1 to Create Account")
print("Press 2 to Withdraw")
print("Press 3 to Deposit")
print("Press 4 to Fund Transfer")
print("Press 5 to Balance Enquiry")
print("Press 6 to Pin Change")
print("Press 7 to Account Summary")
print("Press 8 to Delete Account")
x=int(input("Enter your Choice :"))

if x==1:
    ac="SBI"
    s="select * from account"
    cur.execute(s)
    data=cur.fetchall()
    ct=len(data)
    if ct>0:
        ac=ac+str(ct+101)
    else:
        ac="SBI101"
    p=input("Enter Pin :")
    n=input("Enter Name:")
    f=input("Enter Father's name :")
    e=input("Enter Email :")
    ph=input("Enter Phone :")
    g=input("Enter Gender :")
    c=input("Enter Country :")
    st=input("Enter State :")
    ct=input("Enter City :")
    a=input("Enter Amount :")
    s="insert into account values('"+ac+"','"+p+"','"+n+"','"+f+"','"+e+"','"+ph+"','"+g+"','"+c+"','"+st+"','"+ct+"','"+a+"')"
    cur.execute(s)
    con.commit()
    print("Account Open Succefully with Account Number ",ac)
    
elif x==2:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:
        camt=int(data[0][10]) 
        w=int(input("Enter Amount to Withdraw :"))
        if camt>=w:
            camt=camt-w
            s="update account set amount='"+str(camt)+"' where acno='"+ac+"'"
            cur.execute(s)
            con.commit()
            s="insert into acc_details(acno,amount,date,description)values('"+ac+"','"+str(w)+"','"+str(dt)+"','withdraw')"
            cur.execute(s)
            con.commit()
            print("After withdraw ",w," Your Current balance is = ",camt)
        else:
            print("Insufficient balance")
    else:
            print("Invalid Account or Pin Number !")
            
elif x==3:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:
        camt=int(data[0][10]) 
        w=int(input("Enter Amount to Deposit :"))
        camt=camt+w
        s="update account set amount='"+str(camt)+"' where acno='"+ac+"'"
        cur.execute(s)
        con.commit()
        s="insert into acc_details(acno,amount,date,description)values('"+ac+"','"+str(w)+"','"+str(dt)+"','Deposit')"
        cur.execute(s)
        con.commit()
        print("After Deposit ",w," Your Current balance is = ",camt)                
    else:
        print("Invalid Account or Pin Account !")

elif x==4:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:
        camt=int(data[0][10]) 
        w=int(input("Enter Amount to Transfer :"))
        if camt>=w:
            tac=input("Enter Account Number to transfer :")
            q="select * from account where acno='"+tac+"'"
            cur.execute(q)
            data=cur.fetchall()
            if len(data)>0:
                tamt=int(data[0][10])                        
                camt=camt-w
                tamt=tamt+w
                s="update account set amount='"+str(camt)+"' where acno='"+ac+"'"
                cur.execute(s)
                con.commit()
                s="update account set amount='"+str(tamt)+"' where acno='"+tac+"'"
                cur.execute(s)
                con.commit()
                s="insert into acc_details(acno,amount,date,description)values('"+ac+"','"+str(w)+"','"+str(dt)+"','Transfer')"
                cur.execute(s)
                con.commit()
                s="insert into acc_details(acno,amount,date,description)values('"+tac+"','"+str(w)+"','"+str(dt)+"','Recieve')"
                cur.execute(s)
                con.commit()                        
                print("After Transfer ",w," Your Current balance is = ",camt)
            else:
                print("Invalid Beniciary Accout")
        else:
            print("Insufficient balance")
    else:
        print("Invalid Account or pin Number !")

elif x==5:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:
        camt=int(data[0][10]) 
        print(" Your Current balance is = ",camt)
    else:
        print("Invalid Account or Pin Number !")

elif x==6:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:
        np=input("Enter New Pin :")
        s="update account set pin='"+np+"' where acno='"+ac+"'"
        cur.execute(s)
        con.commit()
        print(" Pin Changed Successfully !")     
    else:
        print("Invalid Account or Pin Number !")

elif x==7:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from acc_details where acno='"+ac+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:                    
        s="select * from acc_details where acno='"+ac+"'"
        cur.execute(s)
        print("S.No\tacc_no\t        amount\tdate\t       description")
        for row in cur:
         print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])             
    else:
        print("Invalid Account Number")
        
elif x==8:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:
        s="delete from account where acno='"+ac+"'"
        cur.execute(s)
        con.commit()
        print(" Deleted !")     
    else:
        print("Invalid Account or Pin Number !")
                    
elif x==0:
    ac=input("Enter Account Number :")
    p=input("Enter Pin Number :")
    s="select * from account where acno='"+ac+"' and pin='"+p+"'"
    cur.execute(s)
    data=cur.fetchall()
    z=len(data)
    if z>0:                    
        s="select * from account where acno='"+ac+"'"
        cur.execute(s)
        print("Ac_No.\tPin\tName\tFather's name\tEmail\t      Phone\tGender\tCountry\tState\tCity\tAmount")
        for row in cur:
         print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6],"\t",row[7],"\t",row[8],"\t",row[9],"\t",row[10])         
    else:
     print("Invalid Account or Pin Number !")
     
else:
    print("Wrong Response !!")