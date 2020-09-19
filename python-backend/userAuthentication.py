#This python program will handle the user authentication from the front end
#Taking a user input of username and password from the front end and then match if the input credentials 
#is valid or not. Display an error message if the credentials are wrong or send the user to a success page if the credential works

def authenticateUser(username, password):
    # #Dictionary to store a list of valid username and password
    users = {"tonyHawk98": "iAmIronMan", 
             "John_Doe": "thisIsME09",
             "Thor69": "Changeme04!"}

    for key, value in users.items():
        if key == username and value == password:
            print("Valid credential")
            break
        else: 
            print("Invalid credential")
            break

    # if username == "tonyHawk98" and password == "iAmIronMan":
    #     print("Valid Credential")
    
    # elif username == "John_Doe" and password == "thisIsME09":
    #     print("Valid Credential")

    # elif username == "Thor69" and password == "Changeme04!":
    #     print("Valid Credential")

    # else: 
    #     print("Invalid Credentials")


    
def main():

    authenticateUser("tonyHawk98", "iAmIronMan")

main()