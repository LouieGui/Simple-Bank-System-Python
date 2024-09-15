import datetime

class bank:
    def __init__(self, fname="", accNo=0, balance=0): 
        self.accNo = accNo
        self.fname = fname
        self.balance = balance
        self.auditTrail = {} 
    
    def __str__(self):
        return f"Account No: {self.accNo} \nFullname: {self.fname} \nBalance: {self.balance:.2f}"
    
    def setBal(self, amount, is_deposit=True, is_initial=False):
        action = "Deposit" if is_deposit else "Withdraw"
        timestamp = datetime.datetime.now().strftime("%B %d | %H:%M:%S")
        year = datetime.datetime.now().strftime("%Y")
        
        if year not in self.auditTrail:
            self.auditTrail[year] = []
        
        if not is_initial:
            self.auditTrail[year].append(f"{timestamp}     -     {action}     -     Balance: {self.balance:.2f}     -     Amount: {amount:.2f}     -     Total: {self.balance + (amount if is_deposit else -amount):.2f}")
        
        self.balance += amount if is_deposit else -amount
    
    def getBal(self):
        return self.balance
        
    def showAuditTrail(self):
        year = datetime.datetime.now().strftime("%Y")
        
        while True:
            print(f"\nAudit Trail for {year}")
            
            if year in self.auditTrail and self.auditTrail[year]:
                for log in self.auditTrail[year]:
                    print(log)
            else:
                print("\nNo Transaction")
            
            exit_choice = input("\nEnter e to exit: ").strip().lower()
            if exit_choice == 'e':
                break

# -----------------------------------------------------------------

# Divider
def divider():
    print("+-----------------------------------+")

# Date
def date():
    current_date = datetime.datetime.now()
    print(current_date.strftime("%B %d, %Y"))

def header():
    print("\nAngelito Louise O. Guiaya")
    date()
    divider()
    print("\t\t\tBanking System")
    divider()

# Temporary Storage 
accounts = {}

# First Menu
def menu():
    while True:
        header()
        print("1. Login \n2. Register \n3. Delete \n4. Show List \n5. Exit")
        divider()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            loginMenu()
        elif choice == "2":
            registerMenu()
        elif choice == "3":
            deleteMenu()
        elif choice == "4":
            forgot()
        elif choice == "5":
            print("Perfect Thanks Bye!")
            break
        else:
            print("Invalid Input! Please choose a number from 1 - 5.")

# Forgot Incase I forgot the account
def forgot():
    header()
    print("List of Accounts\n")
    
    for fname, account in accounts.items():
        print(f"{fname} ---------- {account.getBal():.2f}")
        
    if input("\nDo you want to exit (y/n): ").strip().lower() == 'y':
        menu()

# Login Menu 
def loginMenu():
    header()
    userInput = input("Enter your Fullname: ").strip()
    userAccount = accounts.get(userInput)

    if userAccount:
        mainMenu(userAccount)
    else:
        print("\nYour account doesn't exist")
        if input("Try Again? (y/n): ").strip().lower() == "y":
            loginMenu()

# Register Menu
def registerMenu():
    header()
    fname = input("Enter your Fullname: ").strip()
    
    if fname in accounts:
        print("The account already exists")
        if input("\nTry Again (y/n): ").strip().lower() == "y":
            registerMenu()
    else:
        accNo = len(accounts) + 1
        try:
            balance = 0
            accounts[fname] = bank(fname, accNo, balance)  
            userAccount = accounts[fname]  
            
            if input("\nDo you like to deposit? (y/n): ").strip().lower() == "y":
                while True:
                    try:
                        amount = float(input("Enter the amount: "))
                        userAccount.setBal(amount, is_deposit=True, is_initial=False)
                        break
                    except ValueError:
                        print("\nInvalid Input! Please input a valid number\n")
            print("\nAccount created successfully.")
            mainMenu(userAccount)
        
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")

# Delete Menu
def deleteMenu():
    header()
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
def mainMenu(userAccount):
    while True:
        header()
        print(f"\t\t\t\t\tBalance: {userAccount.getBal():.2f}")
        print("1. Deposit \n2. Withdraw \n3. Audit Trail \n4. Exit")
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
                    userAccount.setBal(amount, False)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            userAccount.showAuditTrail()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Input!")

# Start the program
menu()
