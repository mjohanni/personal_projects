print("Welcome to mJ_login_system.")

def introduction():
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


def get_username_and_password():
    """
    this function gets the username and password of user

    returns: username and password
    """
    user = input("Enter username: ")
    password = input("Enter password: ")
    return (user,password)


if __name__ == '__main__':
    
    choice = introduction()
    print(choice)
    info = get_username_and_password()
    print (info)
