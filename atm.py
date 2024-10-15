balance = 5000  
atmpin = 1234  
print("Welcome to the ATM!")
print("Select your language:")
print("1. English")
print("2. Hindi")
print("3. kannada")
language= int(input("Enter your choice(1/2/3)  "))

if language== 1:
  
    pin = int(input("Enter your 4-digit PIN: "))
    # print("enter the digit")
    # pin=int(input())
    
    if pin == atmpin:
        print("PIN verified.")
        
        # print("Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")

        choice = int(input("Enter your choice (1/2/3) "))

        if choice == 1:
            print("your balance",balance)
        
        elif choice == 2:
            deposit = int(input("Enter amount to deposit: "))
            if deposit > 0:
                balance =balance + deposit
                print('Successfully deposited' ,deposit )
                print("your new balance is:",balance)
            else:
                print("Invalid amount entered.")
            
        elif choice == 3:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if  withdraw_amount <= balance:
                balance =balance- withdraw_amount
                print("Successfully withdrawn ",withdraw_amount) 
                print("Your new balance is: ",balance)
            elif withdraw_amount > balance:
                print("Insufficient balance.")
            else:
                print("Invalid amount entered.")
        
        else:
            print("Invalid choice.")
        
        print("Thank you for using the ATM!")
    
    else:
        print("Incorrect PIN. Please try again.")