import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="yogesh2001",database="bank_mangement")

def  openacc():
    n=input("Enter The Name :")
    ac=input("Enter the account number :  ")
    db= input("Enter the Date Of Birth : ")
    add=input("Enter the address :")
    cn= int(input("Enter the conact number : "))
    ob= int(input("Enter the Opening balance :"))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=("insert into account values(%s,%s,%s,%s,%s,%s)")
    sql2=("insert into amount values(%s,%s,%s)")
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Enter successfully......")
    main()

def depamount():
    amount=int(input("enter the amount you want deposite ::"))
    ac = input("Enter the account number : ")
    a="select balance from amount where accno=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=("update amount set balance=%s where accno=%s")
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def withdrawamount():
    amount = int(input("enter the amount you want withdraw :"))
    ac = input("Enter the account number : ")
    a = "select balance from amount where accno=%s"
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ("update amount set balance=%s where AccNo=%s")
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def  balenquiry():
    ac = input("Enter the account number : ")
    a="select * from amount where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for amount",ac,"is",result[-1])
    main()

def disdetails():
    ac = input("Enter the account number : ")
    a = "select * from account where AccNo=%s"
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def  closeaccount():
    ac = input("Enter the account number : ")
    sql1="delete from account where AccNo=%s"
    sql2="delete from amount where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()


def main():
    print('''
        1.Open new account
        2.Deposite amount
        3.Withdraw amount
        4.Balance enquiry
        5.Display customer details
        6.Closing an account
          ''')
    choice=input("ENTER THE TASK TO PERFORM :")
    if(choice=='1'):
        openacc()
    elif(choice=='2'):
        depamount()
    elif(choice=='3'):
        withdrawamount()
    elif(choice=='4'):
        balenquiry()
    elif(choice=='5'):
        disdetails()
    elif(choice=='6'):
        closeaccount()
    else:
        print("Invalid choice")
main()