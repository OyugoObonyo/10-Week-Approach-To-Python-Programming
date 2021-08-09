"""
A console program that creates a user database with CSV files
"""
import csv


def register_user():
    user_name = input("Please provide your preferred username:  ")
    password = input("Enter preffered password: ")
    password2 = input("Please confirm password: ")


    if password == password2:
        with open("users.csv","a",) as ourdb:
            writer = csv.writer(ourdb, delimiter = ",")
            writer.writerow([user_name,password])
            print(f"Welcome on board {user_name}")
    else:
        print("ERROR: Passwords do not match")
            

def log_in():
    user_name = input("Please provide your username: ")
    password = input("Password: ")
    
    with open("users.csv","r") as ourdb:
        reader = csv.reader(ourdb, delimiter = ",")
        for row in reader:
            if row == [user_name, password]:
                print(f"Welcome back {user_name}")
                return True
        print("ERROR: Incorrect username and/or password")
        return False


def main():
    resume = True

    while resume == True:
        valid_responses = {"REGISTER","LOG IN"}
        user_status = input("Would you like to REGISTER or LOG IN? ")
        if user_status not in valid_responses:
            print("pick only REGISTER or LOG IN")
        if user_status == "REGISTER":
            reg_status = register_user()
        elif user_status == "LOG IN":
            log_status = log_in()

main()
