# ATM Simulation Program

print("===== Welcome to Flywithkhan ATM =====")


pin = "1234"             
balance = 5000.0         

user_pin = input("Enter your 4-digit PIN: ")

if user_pin == pin:
    print("Login successful!\n")
    
    
    while True:
        print("========== MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        
        if choice == "1":
            print(f"Your current balance is ₹{balance:.2f}")
        
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount  
            print(f"₹{amount} deposited successfully!")
            print(f"Updated Balance: ₹{balance:.2f}")
        
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance! ")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully!")
                print(f"Remaining Balance: ₹{balance:.2f}")
        
        elif choice == "4":
            print("Thank you for using Flywithkhan ATM 🏧")
            break
        
        else:
            print("Invalid choice! Please try again.")
        
        print("----------------------------")

else:
    print("Incorrect PIN! Access Denied ❌")
