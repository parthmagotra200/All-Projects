class ATM:
    def __init__(self):
        self.accounts = {'admin': {'password': 'admin', 'balance': 0, 'login_attempts': 0, 'locked': False}}
        self.current_user = None
        self.admin_remaining_attempts = 3

    def create_account(self, user_id, password, balance=0):
        self.accounts[user_id] = {'password': password, 'balance': balance, 'login_attempts': 0, 'locked': False}

    def authenticate(self, user_id, password):
        if user_id == 'admin':
            return self.authenticate_admin(password)
        elif user_id in self.accounts and not self.accounts[user_id]['locked']:
            if self.accounts[user_id]['password'] == password:
                self.current_user = user_id
                self.accounts[user_id]['login_attempts'] = 0
                return True
            else:
                self.accounts[user_id]['login_attempts'] += 1
                remaining_attempts = 3 - self.accounts[user_id]['login_attempts']
                if remaining_attempts > 0:
                    print(f"\nInvalid password. {remaining_attempts} attempts remaining!")
                else:
                    self.accounts[user_id]['locked'] = True
                    print(f"Account {user_id} has been locked due to multiple unsuccessful login attempts!")
                return False
        else:
            return False

    def authenticate_admin(self, password):
        if self.accounts['admin']['password'] == password:
            self.admin_remaining_attempts = 3
            return True
        else:
            self.admin_remaining_attempts -= 1
            if self.admin_remaining_attempts > 0:
                print(f"\nInvalid admin password! {self.admin_remaining_attempts} attempts remaining.")
            else:
                print("Admin account locked due to multiple unsuccessful login attempts!")
                return False
        
    def check_warning(self):
        total_balance = sum(details['balance'] for user_id, details in self.accounts.items() if user_id != 'admin')
        if total_balance < 75000:
            print("\nWarning! The total balance of all users is less than ₹75,000.")

    def deposit(self, amount, denominations):
        if self.current_user is not None:
            if amount > 0 and amount <= 100000:
                total_deposit = 0
                for denomination, count in denominations.items():
                    total_deposit += denomination * count
                if total_deposit == amount:
                    self.accounts[self.current_user]['balance'] += amount
                    return True
                else:
                    print("Invalid denominations! Please provide correct denominations.")
            else:
                print("\nInvalid deposit amount! Deposit amount should be between 1 and 100,000.")
        else:
            print("User not authenticated! Please log in first.")
        return False

    def withdraw(self, amount, denominations):
        if self.current_user is not None:
            if amount > 0 and amount <= 50000:
                total_withdraw = 0
                for denomination, count in denominations.items():
                    total_withdraw += denomination * count
                if total_withdraw == amount and amount <= self.accounts[self.current_user]['balance']:
                    self.accounts[self.current_user]['balance'] -= amount
                    return True
                elif amount > self.accounts[self.current_user]['balance']:
                    print("Insufficient funds!")
                else:
                    print("Invalid denominations! Please provide correct denominations.")
            else:
                print("Invalid withdrawal amount! Withdrawal amount should be between 1 and 50,000.")
        else:
            print("User not authenticated! Please log in first.")
        return False

    def check_balance(self):
        if self.current_user is not None:
            return self.accounts[self.current_user]['balance']
        else:
            print("User not authenticated! Please log in first.")
            return None

    def change_password(self, current_password, new_password):
        if self.current_user is not None:
            if self.accounts[self.current_user]['password'] == current_password:
                self.accounts[self.current_user]['password'] = new_password
                print("\nPassword changed successfully.")
                return True
            else:
                print("Incorrect current password! Password not changed.")
        else:
            print("User not authenticated! Please log in first.")
        return False  

    def view_all_users(self, admin_password):
        if self.authenticate('admin', admin_password):
            print(f"\nUser Accounts: ")
            for user_id, details in self.accounts.items():
                if user_id != 'admin':
                    print(f"User ID: {user_id}, Balance: ₹{details['balance']}, Locked: {details['locked']}")
            if self.admin_remaining_attempts < 3:
                print(f"Remaining admin login attempts: {self.admin_remaining_attempts}")

            self.check_warning()
        else:
            print("Admin authentication failed! Please check the password.")    
            
def welcome_interface():
    print("Welcome to the ATM System!")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    return choice

atm = ATM()
atm.create_account('user1', 'password1', 10000)
atm.create_account('user2', 'password2', 8000)
atm.create_account('user3', 'password3', 15000)
atm.create_account('user4', 'password4', 20000)
atm.create_account('user5', 'password5', 30000)

while True:
    choice = welcome_interface()

    if choice == '1':
        user_id = input("Enter your user ID: ")
        password = input("Enter your password: ")
        if atm.authenticate(user_id, password):
            print("Authentication successful")
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Change Password")
                print("5. Exit")
                user_choice = input("Enter your choice (1-5): ")
                if user_choice == '1':
                    amount = int(input("Enter the deposit amount: ₹"))
                    denominations = {
                        100: int(input("Enter the number of ₹100 bills: ")),
                        200: int(input("Enter the number of ₹200 bills: ")),
                        500: int(input("Enter the number of ₹500 bills: ")),
                        2000: int(input("Enter the number of ₹2000 bills: "))
                    }
                    if atm.deposit(amount, denominations):
                        print("Deposit successful.")
                    else:
                        print("Deposit failed!")

                elif user_choice == '2':
                    amount = int(input("Enter the withdrawal amount: ₹"))
                    denominations = {
                        100: int(input("Enter the number of ₹100 bills: ")),
                        200: int(input("Enter the number of ₹200 bills: ")),
                        500: int(input("Enter the number of ₹500 bills: ")),
                        2000: int(input("Enter the number of ₹2000 bills: "))
                    }
                    if atm.withdraw(amount, denominations):
                        print("Withdrawal successful.")
                    else:
                        print("Withdrawal failed.")

                elif user_choice == '3':
                    balance = atm.check_balance()
                    if balance is not None:
                        print("\nBalance: ₹{}".format(balance))

                elif user_choice == '4':
                    current_password = input("Enter your current password: ")
                    new_password = input("Enter your new password: ")

                    atm.change_password(current_password, new_password)

                elif user_choice == '5':
                    print("\nExiting user interface. Thank you!")
                    break

                else:
                    print("\nInvalid choice! Please enter a number between 1 and 5.")

    elif choice == '2':
        admin_password = input("Enter the admin password: ")
        if atm.authenticate('admin', admin_password):
            print("\nLogin Successful\n")
            admin_choice = input("1. View All User Accounts\n2. Exit Admin Interface\nEnter your choice (1-2): ")
            if admin_choice == '1':
                atm.view_all_users(admin_password)
                print("\n")
            elif admin_choice == '2':
                print("\nExiting admin interface. Thank you!")
            else:
                print("\nInvalid choice! Please enter a number between 1 and 2.")
        else:
            if atm.admin_remaining_attempts == 0:
                break

    elif choice == '3':
        print("\nExiting. Thank you!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 3.")


