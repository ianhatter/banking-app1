from banking_pkg import account


def atm_menu(name):
    print("")
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
print("User: " + name)
pin = input("Enter pin: ")
balance = str(0)
print(name, " has been registured with a starting balance of $", balance)

while True:
    print("LOGIN")
    user_name = input("Enter Username: ")
    Pin = input("Enter Pin:")
    if user_name == "imh" and pin == "334":
        print("Login successful! ")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(user_name)
    option = input("Choose option:")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)

    else:
        option == "4"
        account.logout(name)


atm_menu(name)
