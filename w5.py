# --- Back End Code ---
pin = 8888
balance = 10000
transaction_history = []  # Tracks user actions

def verify_pin():
    """Helper function to handle PIN verification with a 3-attempt limit."""
    attempts = 0
    while attempts < 3:
        try:
            check_pin = int(input("\t\t\tENTER YOUR PIN NUMBER: "))
            if check_pin == pin:
                return True
            else:
                attempts += 1
                print(f"\t\t\tWRONG PIN. {3 - attempts} attempts remaining.")
        except ValueError:
            print("\t\t\tInvalid input. Please enter numbers only.")
            attempts += 1
    print("\t\t\tCARD BLOCKED. Please contact your bank.")
    return False

def show_balance_option():
    """Helper function to ask if user wants to see their current balance."""
    check = input("\t\t\tDO YOU WANT TO KNOW YOUR BALANCE(Y/N): ").upper()
    if check == 'Y':
        print(f"\t\t\tYOUR BALANCE: ${balance}")

def withdraw_amount():
    global balance
    print("\t\t\tINSERT YOUR ATM CARD........... ")
    if not verify_pin():
        return

    try:
        w_amount = int(input("\t\t\tENTER THE AMOUNT TO BE WITHDRAWN: "))
        if w_amount <= balance:
            if w_amount % 10 != 0:
                print("\t\t\tPlease enter an amount in multiples of 10.")
                return
            balance -= w_amount
            transaction_history.append(f"Withdrew: -${w_amount}")
            print("\t\t\tYOUR TRANSACTION IS IN PROGRESS........... ")
            print("\t\t\tCASH WITHDRAWAL SUCCESSFUL........ ")
            show_balance_option()
        else:
            print("\t\t\tINSUFFICIENT BALANCE.")
    except ValueError:
        print("\t\t\tInvalid amount entered.")

def deposit_amount():
    global balance
    print("\t\t\tINSERT YOUR ATM CARD............. ")
    if not verify_pin():
        return

    try:
        d_amount = int(input("\t\t\tENTER THE AMOUNT TO BE DEPOSITED: "))
        if d_amount > 0:
            balance += d_amount
            transaction_history.append(f"Deposited: +${d_amount}")
            print("\t\t\tAMOUNT DEPOSITED SUCCESSFULLY!")
            show_balance_option()
        else:
            print("\t\t\tInvalid deposit amount.")
    except ValueError:
        print("\t\t\tInvalid input.")

def balance_amount():
    print("\t\t\tINSERT YOUR ATM CARD.......... ")
    if not verify_pin():
        return
    print(f"\t\t\tYOUR BALANCE: ${balance}")

def fast_cash():
    global balance
    print("\t\t\tINSERT YOUR ATM CARD.......... ")
    if not verify_pin():
        return
    
    print("\t\t\t1. $20 \t 2. $50 \t 3. $100")
    try:
        choice = int(input("\t\t\tSELECT FAST CASH OPTION: "))
        amounts = {1: 20, 2: 50, 3: 100}
        
        if choice in amounts:
            amt = amounts[choice]
            if amt <= balance:
                balance -= amt
                transaction_history.append(f"Fast Cash: -${amt}")
                print(f"\t\t\tSUCCESSFULLY WITHDREW ${amt}!")
                show_balance_option()
            else:
                print("\t\t\tINSUFFICIENT BALANCE.")
        else:
            print("\t\t\tINVALID OPTION.")
    except ValueError:
        print("\t\t\tInvalid input.")

def change_pin():
    global pin
    print("\t\t\tINSERT YOUR ATM CARD.......... ")
    if not verify_pin():
        return
    
    try:
        new_pin = int(input("\t\t\tENTER YOUR NEW 4-DIGIT PIN: "))
        confirm_pin = int(input("\t\t\tCONFIRM YOUR NEW PIN: "))
        
        if new_pin == confirm_pin:
            if 1000 <= new_pin <= 9999:
                pin = new_pin
                print("\t\t\tPIN CHANGED SUCCESSFULLY!")
            else:
                print("\t\t\tPIN MUST BE A 4-DIGIT NUMBER.")
        else:
            print("\t\t\tPIN MISMATCH. OPERATION CANCELED.")
    except ValueError:
        print("\t\t\tInvalid input.")

def view_mini_statement():
    print("\t\t\tINSERT YOUR ATM CARD.......... ")
    if not verify_pin():
        return
        
    print("\t\t\t--- MINI STATEMENT ---")
    if not transaction_history:
        print("\t\t\tNo recent transactions.")
    else:
        for tx in transaction_history[-5:]: # Show last 5 transactions
            print(f"\t\t\t{tx}")
    print(f"\t\t\tCURRENT BALANCE: ${balance}")

# --- Front End Code ---
print("\t\t\t===============================")
print("\t\t\t      Welcome to the ATM       ")
print("\t\t\t===============================")

op = 'Y'
while op == 'Y':
    print("\n\t\t\t1. Withdraw Amount")
    print("\t\t\t2. Deposit Amount")
    print("\t\t\t3. Balance Check")
    print("\t\t\t4. Fast Cash")
    print("\t\t\t5. Change PIN")
    print("\t\t\t6. Mini Statement")
    
    try:
        a = int(input("\n\t\t\tENTER YOUR OPTION: "))
        if a == 1:
            withdraw_amount()
        elif a == 2:
            deposit_amount()
        elif a == 3:
            balance_amount()
        elif a == 4:
            fast_cash()
        elif a == 5:
            change_pin()
        elif a == 6:
            view_mini_statement()
        else:
            print("\t\t\tINVALID OPTION.....")
    except ValueError:
        print("\t\t\tPlease enter a valid choice number.")
        
    op = input("\n\t\t\tDO YOU WANT TO DO ANOTHER TRANSACTION? (Y/N): ").upper()

print("\t\t\tTHANK YOU FOR USING OUR ATM. GOODBYE!")
