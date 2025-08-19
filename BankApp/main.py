import auth

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
    
landingPage()