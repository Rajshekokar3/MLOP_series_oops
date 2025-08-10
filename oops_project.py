class chatbook:
    __user_id=0
    def __init__(self):
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        self.__username="hello daddy" # hidden attribute  or we can say privac 
        self.password =""
        self.loggedin=False
    # using static method directly from class rather than object
    @staticmethod
    def get_id(): # when we are creating static method we dont give static method and for accesing it dont requied object
        return chatbook.__user_id
    
    @staticmethod
    def set_id(values):# when we are creating static method we dont give static method and for accesing it dont requied object
        chatbook.__user_id=values
    
    
    def get_name(self):
        return self.__username
    
    def set_name(self,value):
        self.__username=value
        
    
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
            self.post()
        elif user_input == "4":
            self.sendmsg()
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

    def post(self):
        if self.loggedin==True:
            txt=input("Enter your message here")
            print("Following content has been  posted")
        else:
            print("You need to Signed in first to post somthing ")
            self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here")
            frnd=input("Whom to send mesage") 
            print(f"Your mesage has been sent to {frnd}")
        else:
            print("Signned in first")
            self.menu()   

