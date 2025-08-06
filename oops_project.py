class chatbook:
    def __init__(self):
        self.username=""
        self.password =""
        self.loggedin=False
        self.menu()
    
    def menu(self):
        user_input=input("""Welcome to chatbooks !! How would you like to proced?
                               1. Press 1 to singup
                               2. Press 2 to signin
                               3. Press 3 to  write a post
                               4. Press 4 to  message a friend
                               5. Press any other key to exits """)
        if user_input== "1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


    def signup(self):
        email=input("Enter your emails\n")
        Password=input("Setup your password \n")
        self.username =email
        self.password = Password
        print("You have Signup succes fully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please Signup by pressing 1 in the main menu")
        else :
            usernam =input("Enter your email/username")
            pwd =input("Enter you passsword")

            if self.username ==usernam  and self.password ==pwd:
                print("You have signed in succesfully !!")
                self.loggedin =True
            else:
                print("Please input correct credentials....")
        print("\n")
        self.menu()

obj=chatbook()