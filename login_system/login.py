import json
import getpass
from save_client_info import save_info

#globals
with open("accounts.json","r+") as file:
    accounts = json.load(file)


def  introduction():
    """
    starting program to decide weather user wants to 
    log in or create a new account
    """
    user_input = input("""would you like to:
1: Create a new account?
2: sign in?
type "exit" to quit program
: """)
    if user_input.isdigit() == True and int(user_input) > 0 and int(user_input) < 3:
        return user_input
    elif user_input == 'exit':
        exit()
    else:
        print("error! incorrect choice. please select appropriate response")
        return introduction()


def register():
    """
    when a user selects register option
    should check list for username in accounts file
    if it does match return false 
    else return true
    """
    username = input("please enter username: ")
    password1 = getpass.getpass("now enter password: ")
    password2 = getpass.getpass("retype password: ")
    while password1 != password2:
        print("passwords do not match. please try again")
        password1 = getpass.getpass("now enter password: ")
        password2 = getpass.getpass("retype password: ")
    return(username,password1)


def  get_login_info():

    """
    this function gets the username and password of user

    returns: username and password
    """
    user = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    return (user,password)


def check_accounts(choice):
    """
    choice will be used to determine which check will be
    executed.
    checks weather username is in account file
    if subscribing the check will compare usernames.
        returns: false if username not in dict
        returns: true if username is in dict
    else if user is logging in it will check usernames and 
    if that username matches the password should match as well.
        returns: true if username and password match
        returns: false if username or password don't match
    """
    global accounts
    if int(choice) == 1:
        info = register()
        for acc_name in accounts:
            if info[0] == acc_name:
                print("Sorry that account already exists, please try again or log in.")
                return False
        print("saving user data...")
        save_info(info[0],info[1])
        print("registered successfully!")
        return True

    elif int(choice) == 2:
        info = get_login_info()
        for acc_name in accounts:
            if info[0] == acc_name:
                if info[1] == accounts[acc_name]:
                    print("Login successful!")
                    return True
        print("Please enter valid username/password.")
        return False


def run_login():
    choice = introduction()
    output = check_accounts(choice)
    if output == False:
        return run_login()
    print("you have successfully registered/logged in.")


if  __name__ == '__main__':
    print("Welcome to mJ_login_system.")
    run_login()
