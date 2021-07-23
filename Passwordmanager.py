from cryptography.fernet import Fernet

master_pwd=input("What is your master password? ")

def view():
    with open("home.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print("Username is:", user, "Password is:", passw)

def add():
    name=input("Enter your account number:")
    pwd=input("Enter your password:")

    with open("home.txt","a") as f:
        f.write(name+ " | " +pwd+ " \n")

while True:
    mode=input("Would you like to add a new passowrd or view existing ones(view, add), press q to quit? ")

    if mode=='q':
        break
    
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")