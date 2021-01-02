import json

def  introduction():
    """
    starting program to decide weather user wants to 
    log in or create a new account
    """
    user_input = input("""would you like to:
1) Create a new account?
2) sign in?
type "exit" to quit program
: """)
    if user_input.isdigit() == True and int(user_input) > 0 and int(user_input) < 3:
        return user_input
    elif user_input == 'exit':
        return 0
    else:
        print("error! incorrect choice. please select appropriate response")
        return introduction()


def subscribe():
    """
    when a user selects subscribe option
    should check list for username in accounts file
    if it does match return false 
    else return true
    """
    username = input("please enter username: ")
    password1 = input("now enter password: ")
    password2 = input("retype password: ")
    while password1 != password2:
        print("passwords do not match. please try again")
        password1 = input("now enter password: ")
        password2 = input("retype password: ")
    return(username,password1)


def check_accounts(username,password,choice):
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
    
    pass


def  get_username_and_password():
    """
    this function gets the username and password of user

    returns: username and password
    """
    user = input("Enter username: ")
    password = input("Enter password: ")
    return (user,password)


def run_log():
    print("Welcome to mJ_login_system.")
    pass


if  __name__ == '__main__':
    
    choice = introduction()
    print(choice)
    info = get_username_and_password()
    print (info)
