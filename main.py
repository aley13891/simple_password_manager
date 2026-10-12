import json
import os

accounts = []

def start():
    global accounts
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    else:
        print("accouts file doesn't exists")        

def json_list():
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
    

 
def search():
    user_name = input("enter username you want: ")

    result = False

    for account in accounts:
        if account["username"] == user_name:
            print("username:", account["username"])
            print("password:", account["password"])
            result = True
            break

    if result == False:
        print("the username not found")


def all_accounts():
    for account in accounts:
        print("username:", account["username"])
        print("password:", account["password"])


def add_account():
    found = False
    username = input("username: ")
    password = input("password: ")
    for account in accounts:
        if account["username"] == username:
            found = True
            break
    if found:
        print("the user name is already used")
    else:
        accounts.append({"username": username, "password": password})    
        json_list()        

def del_account():
    username = input("enter the username you want to delete: ")  
    found = False
    for account in accounts:
        if account["username"] == username:
            found = True
            break
        
    if found:
        accounts.remove(account)
        json_list()
        print("the account has been deleted")
    else:
        print("there is no account with this username")
            

def main():
    while True:
        main_menu = input("\n\n1. search for accounts\n2. show all accounts\n3. add account\n4. delete account\n5. exit\n\n answer: ")
        if main_menu == "1":
            search()
        elif main_menu == "2":
            all_accounts()
        elif main_menu == "3":
            add_account()
        elif main_menu == "4":
            del_account()
        elif main_menu == "5":
            break
        else:
            print("error! type(1,2,3,4,5)")

try:
    start()
    main()
except FileNotFoundError:
    print("json file doesn't exist")
except :
    print("\nsomething went wrong")    