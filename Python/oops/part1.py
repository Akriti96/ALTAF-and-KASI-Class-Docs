class ATM:
    def __init__(self):
        self.__pin="12345"  # private variable
        self.__balance=100
        # self.menu()

    # getter method
    def get_pin(self):
        return self.__pin
    
    # setter method
    def set_pin(self,pin):
        self.__pin=pin
     
    def getBalance(self):
        return self.__balance


class Student:
    def add(self,a1,a2):
        return a1+a2


# sbi account -- (address, ifsc, email, phone)
# print(a1.get_pin())
# a1.set_pin("7890")
# print(a1.get_pin())



    # def get_balance(self):
    #     return f"The balance is {self.balance}"
        
    # def menu(self):
    #     user_input=int(input("Hii how can i help u " 
    #     "1. Create a pin\n"
    #     "2. withdraw\n"
    #     "3  check Balance\n"
    #     "4. change pin\n"
    #     "5 exit :  "))
    #     try:
    #         if isinstance(user_input,int):
    #             if user_input == 1:
    #                 self.create_pin()
    #             elif user_input == 4:
    #                 self.change_pin()
    #             elif user_input == 2:
    #                 self.withdraw()
    #             elif user_input == 3:
    #                 self.deposit()
    #             else:
    #                 print("wrong choice!")
    #     except Exception as e:
    #         print("enter the valid choice")
    #         self.menu()
        
    # def create_pin(self):
    #     user_pin= int(input("Enter your pin btw 1 to 9: "))
    #     self.pin=user_pin
    #     print(f"Pin is created {self.pin}")
    #     self.menu()
        
    # def change_pin(self):
    #     old_pin=int(input("Enter your old pin: "))
    #     if old_pin == self.pin:
    #         new_pin=int(input("Enter your new pin btw 1 to 9: "))
    #         self.pin= new_pin
    #         print(f"New Pin is created {self.pin}")
    #     else:
    #         print("The pin u entered is wrong")
    #         self.menu()
        
    # def withdraw(self):
    #     user_pin= int(input("Enter your pin btw 1 to 9: "))
    #     if user_pin == self.pin:
    #         amount= int(input("Enter the amount to with draw: "))
    #         if amount <= self.balance:
    #             self.balance= self.balance-amount
    #             print(f"{amount} withdrawed and balance is {self.get_balance()}")
    #             self.menu()
    #         else:
    #             print("in sufficient balance")

    #     else:
    #         print("wrong pin entered")
    #         self.men()

    # def deposit(self):
    #     user_pin= int(input("Enter your pin btw 1 to 9: "))
    #     if user_pin == self.pin:
    #         amount= int(input("Enter the amount to with deposit: "))
    #         self.balance= self.balance+amount
    #         print(f"{amount} deposited and balance is {self.get_balance()}")
    #         self.menu()
    #     else:
    #         print("wrong pin entered")
    #         self.men()

# for i in range(10):
#     i= ATM()
#     print(i)