import json

def save_info(username,password):
    """Creates a json file and stores the user's information"""
    user_dict = {username : password}
    with open("accounts.json", "r+") as file:
        f = json.load(file)
        f.update(user_dict)
        file.seek(0)
        json.dump(f,file)
