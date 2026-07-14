# Bank Account

print("======Welcome To Python Bank======")

# Register

users = {
    "Walaa": {"password": "123456", "balance": 0},
    "Mostafa": {"password": "323758", "balance": 0},
    "Mohamed": {"password": "00000000", "balance": 0},
    "Ibrahim": {"password": "976532464", "balance": 0},
    "Aisha": {"password": "554432256", "balance": 0}
}


def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "" or password == "":
        print("Empty input is not allowed.")
        return

    if username in users:
        print("Username already exists.")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return

    users[username] = {
        "password": password,
        "balance": 0
    }

    print("Account created successfully!")


# Login

def login():
    user_name = input("Enter Username: ")
    password = input("Enter Password: ")

    if user_name not in users:
        print("Username does not exist.")
        return

    if users[user_name]["password"] != password:
        print("Incorrect password.")
        return

    print(f"Welcome {user_name}")
    bank_menu(user_name)


# Bank Menu

def bank_menu(user_name):
    while True:
        print("\n========== Bank Menu ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Change Password")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(user_name)

        elif choice == "2":
            deposit(user_name)

        elif choice == "3":
            withdraw(user_name)

        elif choice == "4":
            transfer(user_name)

        elif choice == "5":
            change_password(user_name)

        elif choice == "6":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice.")


# Check Balance

def check_balance(user_name):
    print(f"Your Balance: {users[user_name]['balance']} EGP")


# Deposit

def deposit(user_name):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    users[user_name]["balance"] += amount
    print("Deposit successful.")
    print(f"Current Balance: {users[user_name]['balance']} EGP")


# Withdraw

def withdraw(user_name):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > users[user_name]["balance"]:
        print("Insufficient balance.")
        return

    users[user_name]["balance"] -= amount
    print("Withdraw successful.")
    print(f"Current Balance: {users[user_name]['balance']} EGP")


# Transfer

def transfer(user_name):
    receiver = input("Enter recipient username: ")

    if receiver not in users:
        print("Username does not exist.")
        return

    if receiver == user_name:
        print("You cannot transfer to yourself.")
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > users[user_name]["balance"]:
        print("Insufficient balance.")
        return

    users[user_name]["balance"] -= amount
    users[receiver]["balance"] += amount

    print("Transfer successful.")
    print(f"Current Balance: {users[user_name]['balance']} EGP")


# Change Password

def change_password(user_name):
    current_password = input("Enter current password: ")
    new_password = input("Enter new password: ")

    if users[user_name]["password"] != current_password:
        print("Incorrect current password.")
        return

    if len(new_password) < 6:
        print("Password must be at least 6 characters long.")
        return

    users[user_name]["password"] = new_password
    print("Password changed successfully.")


# Main Menu

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank you for using Python Bank.")
        break

    else:
        print("Invalid choice.") 