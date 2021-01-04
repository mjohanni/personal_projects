# import json
# from save_client_info import save_info
import getpass

# if __name__ == "__main__":
#     save_info("matthew1","19940621mayheM.")
#     save_info("matthew11","19940621mayheM.")
#     save_info("matthew2","19940621mayheM.")
#     save_info("matthew3","19940621mayheM.")
#     save_info("jeff","123J123")
    # with open("accounts.json", "r+") as file:
    #     my_accounts = json.load(file)
    # for item in my_accounts:
    #     print(item)


username = "matthew"

password = getpass.getpass("enter password: ")
print(password)