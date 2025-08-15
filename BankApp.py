import getpass

def register():
    print("===Register===")
    username = input("Enter your username:")
    pin = getpass.getpass("Enter your PIN:")
    
    if pin.isdigit() and len(pin) == 4:
        print("PIN Accepted. Ready to log-in!")
        return username, pin
        
    else:
        print("Invalid input. please exactly put 4 digits")
        return None, None
        
def login(storedPin, storedUsername):
    while True:
        print("===LOGIN===")
        userUsernameInput = input("Enter your username:")
        userPinInput = getpass.getpass("Enter your PIN:")
    
        if userUsernameInput != storedUsername:
            print("Incorrect username, please be sure you registered your account.")
            break
        
        if userPinInput != storedPin:
            print("Incorrect PIN input!")
            break
        
    
        print("Login Successful!")
        break
        
def landingPage():
    while True:
        print("1.Register \n2.Login \n3.Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            username, pin = register()
        elif choice == '2':
            if username and pin:
                login(username, pin)
            else:
             print("No users registered yet.")
        elif choice == '3':
            print("Exiting...")
            exit()
        else:
            print("Please input 1-3 only.")
            break

landingPage()