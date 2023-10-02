class Bank:

    def getdata(self):
        self.ano = int(input("Enter Your Acc no : "))
        self.name = input("Enter Your Name : ")
        self.bal = int(input("Enter Your Total Balance : "))
    def showdata(self):
        print("Your Acc no : ",self.ano)
        print("Your Name is : ",self.name)
        print("Your amount is : ",self.bal)
    def deposit(self):
        self.depo = int(input("Enter your amount that you want to deposit : "))
        self.bal = self.depo + self.bal

    def withdrawal(self):
        self.wd = int(input("Enter your amount that you want to withdrwwal : "))
        if(self.bal >= self.wd):
            self.bal = self.bal - self.wd
        else:
            print("Sorry You can not withdrawal your amount you can withdrawal amount within your total amount in your account is : ", self.bal)
            l[i].withdrawal()
l = [0,0,0,0,0]
for i in range(0,5,1):
    l[i] = Bank()
p=0
a=0
while(a!=5):
    print("1 . Please Enter details")
    print("2 . Show details")
    print("3 . Deposit")
    print("4 . Withdrawal")
    print("5 . Exit")
    a = int(input("Enter Your choice : "))
    if(a == 1):
        l[p].getdata()
        p=p+1
    elif(a == 2):
        for i in range(0,p,1):
            l[i].showdata()
    elif(a == 3):
        acc_no = int(input("Enter your Account no : "))
        found = 0
        for i in range(0,p,1):
            if(l[i].ano == acc_no):
                l[i].deposit()
                found = 1
        if(found != 1):
            print("Not matched your acc with data base")
    elif(a == 4):
        acc_no = int(input("Enter your Account no : "))
        found = 0
        for i in range(0,p,1):
            if(l[i].ano == acc_no):
                l[i].withdrawal()
                found = 1
        if(found != 1):
            print("Not matched your acc with data base")

