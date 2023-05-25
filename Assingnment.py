Mail = input ("Please enter your email;")
while True :
    
    PIN = input("Please create a PIN to use during Login;")
    Confirm_PIN = input("Reconfirm PIN;")

    if PIN == Confirm_PIN:
        break
        print(AccountCreatedsuccessfully)

    if PIN != Confirm_PIN:
        continue
        print(wrong)
