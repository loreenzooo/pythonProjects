import getpass as gp

def register():
    print("=== Register ===")
    username = input("Enter your username: ")
    pin = gp.getpass("Enter your PIN (4 digits): ")

    if pin.isdigit() and len(pin) == 4:
        print("PIN Accepted. Ready to log in!")
        return username, pin            
    else:
        print("Invalid input. Please enter exactly 4 digits.")
        return None, None              

def login(username, pin):
    print("=== LOGIN ===")
    userUsernameInput = input("Enter your username: ")
    userPinInput = gp.getpass("Enter your PIN: ")

    if userUsernameInput != username:
        print("Incorrect username, please be sure you registered your account.")
        return False

    if userPinInput != pin:
        print("Incorrect PIN input!")
        return False

    print("Login Successful!")
    return True                          

def landingPage():
    username = None
    pin = None
    isLoggedIn = False                   

    while True:
        print("\n1. Register \n2. Login \n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username, pin = register()   

        elif choice == '2':
            if username and pin:         
                isLoggedIn = login(username, pin)   
                if isLoggedIn:                       
                    print("Hello")
                    break
            else:
                print("No users registered yet.")

        elif choice == '3':
            print("Exiting...")
            exit()

        else:
            print("Please input 1-3 only.")

