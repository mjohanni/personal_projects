import json

def save_info(username,password):
    """Creates a json file and stores the user's information"""

    user_dict = {username : password}
    file = json.dumps(user_dict)
    f = open("accounts.json", "w")
    f.write(file)
    f.close()