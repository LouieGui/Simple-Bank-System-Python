class bank:
    def __init__(self, fname="", accNo = 0, balance = 0): 
        self.accNo = accNo
        self.fname = fname
        self.balance = balance
    
    def __str__(self):
        return f"Account No: {self.accNo} \nFullname: {self.fname} \nBalance: {self.balance:.2f}"
    
    def setBal(self, amount, is_deposit=True):
        self.balance += amount if is_deposit else -amount
    
    def getBal(self):
        return self.balance

# ----------------------------------------------------------------------------------------------------------

# Divider
def divider():
    print("+-----------------------------------+")

# Date
import datetime
def date():
    current_date = datetime.datetime.now()
    print(current_date.strftime("%B %d, %Y"))

# Temporary Storage 
accounts = {}

# First Menu
def menu():
    while True:
        print("\nAngelito Louise O. Guiaya")
        date()
        divider()
        print("\t\t\tBanking System")
        divider()
        print("1. Login \n2. Register \n3. Delete")
        divider()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            loginMenu()
        elif choice == "2":
            registerMenu()
        elif choice == "3":
            deleteMenu()
        else:
            print("Invalid Input! Please a number from 1 - 3.")

# Login Menu 
def loginMenu():
    print("\nAngelito Louise O. Guiaya")
    date()
    divider()
    print("\t\t\tBanking System")
    divider()
    userInput = input("Enter your Fullname: ").strip()
    userAccount = accounts.get(userInput)

    if userAccount:
        main_menu(userAccount)
    else:
        print("\nYour account doesn't exist")
        if input("Try Again? (y/n): ").strip().lower() == "y":
            loginMenu()

# Register Menu
def registerMenu():
    print("\nAngelito Louise O. Guiaya")
    date()
    divider()
    print("\t\t\tBanking System")
    divider()
    fname = input("Enter your Fullname: ").strip()
    accNo = len(accounts) + 1

    try:
        balance = 0
        if input("\nDo you like to deposit? (y/n): ").strip().lower() == "y":
            balance = float(input("Enter the amount: "))
        
        accounts[fname] = bank(fname, accNo, balance)
        print("\nAccount created successfully.")
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")

# Delete Menu
def deleteMenu():
    print("\nAngelito Louise O. Guiaya")
    date()
    divider()
    print("\t\t\tBanking System")
    divider()
    fname = input("Enter your Fullname: ").strip()
    userAccount = accounts.get(fname)

    if userAccount:
        print(userAccount)
        if input("\nAre you sure you want to delete? (y/n): ").strip().lower() == "y":
            del accounts[fname]
            divider()
            print("Account deleted successfully.")
    else:
        print("\nAccount does not exist.")

# Main Menu
def main_menu(userAccount):
    while True:
        print("\nAngelito Louise O. Guiaya")
        date()
        divider()
        print("\t\t\tBanking System")
        divider()
        print(f"\t\t\t\t\tBalance: {userAccount.getBal():.2f}")
        print("1. Deposit \n2. Withdraw \n3. Exit")
        divider()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                userAccount.setBal(amount, True)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))

                if userAccount.getBal() == 0:
                    print("No Money!")
                elif amount > userAccount.getBal():
                    print("Sobra na")
                else:
                    userAccount.getBal(amount, False)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid Input!")

# Start the program
menu()
