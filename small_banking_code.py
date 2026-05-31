class bankacc():
    bank={}
    def __init__(self,name,balance,acc_no):
         self.__name=name
         self.__acc_no=acc_no
         self.__balance=balance
        
    def create_acc(self):
        
        self.bank[self.__name]={
             "acc_no":self.__acc_no,
             "balance":self.__balance
             }
    def details(self):
        if self.__name in self.bank:
            print(self.__acc_no)
            print(self.__balance)
        else:
             print(f'invalid name,{name} not fount')

    def deposite(self,deposite=0):
            self.__balance+=deposite
            print(f" deposited amount to {self.__acc_no} acc_no is {deposite}rs. The balance is {self.__balance}rs")
           
    def withdraw(self,withdraw):
        self.__balance-=withdraw
        print(f"withdrawed amount from {self.__acc_no} acc_no is {withdraw}rs. The balance is {self.__balance}rs")

name=input("enter the name: ")
acc_no=int(input("Acc_no: "))
balance=int(input("Balance: "))
bha=bankacc(acc_no,balance,name)
bha.create_acc()
bha.details()
bha.deposite(14000)
bha.withdraw(int(input('withdraw: ')))
