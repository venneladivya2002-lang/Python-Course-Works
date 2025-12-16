import ATM

account_number=input("Enter the account_number: ")
pin=input("Enter the pin: ")

if ATM.login(account_number,pin):
    while True:
        ATM.display_menu()
        ch=int(input("Enter the choice: "))
        if ch==1:
            ATM.check_balance()
        elif ch==2:
            ATM.deposit_money()
        elif ch==3:
            ATM.withdraw_money()
        elif ch==4:
            ATM.show_transactions()
        elif ch==5:
            print("Thankyou, Bye!!!!")
            break
        else:
            print("Enter the valid choice")

            
