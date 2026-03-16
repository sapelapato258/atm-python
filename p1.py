try:
    with open("balance.txt", "r") as file:
        balance = int(file.read())
except FileNotFoundError:
    balance = 1000
    with open("balance.txt", "w") as file:
        file.write(str(balance))

print(f"Starting balance: ₹{balance}")
while True:
    print(f"\nCurrent balance: {balance}")
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Exit")
    
    choice = input("Enter choice(1/2/3): ") 
    
    if choice == "1":  
        amount = int(input("Enter amount to Withdraw: ")) 
        if amount > balance:
            print("insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawn {amount}. New balance: {balance}")
            with open("balance.txt", "w") as file:
                file.write(str(balance))
    
    elif choice == "2":
        amount = int(input("Enter amount to Deposite: "))
        balance += amount
        print(f"Deposited {amount}. New balance: {balance}")
        with open("balance.txt", "w") as file:
            file.write(str(balance))
    
    elif choice == "3": 
        print("Thank you for using our ATM!")
        break
    
    else:  
        print("Invalid choice! Please choose among 1, 2, or 3.")
