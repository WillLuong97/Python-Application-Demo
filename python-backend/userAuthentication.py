#This python program will handle the user authentication from the front end
#Taking a user input of username and password from the front end and then match if the input credentials 
#is valid or not. Display an error message if the credentials are wrong or send the user to a success page if the credential works

import http.server
from http.server import BaseHTTPRequestHandler
import json
import requests
import urllib.parse

class RequestListner(BaseHTTPRequestHandler):
    def doPost(self):
        #function to listen for a POST request from the Front-end
        path = self.path

        #Displaying the header of the path being sent in
        print("Headers: ", self.headers, "")
        print("Domain: ", self.headers['host'])

        #Displaying the type of the content in the request
        print("Content-Type: ", self.headers['Content-type'])

        #Collecting the length of the body read the characters that are contained in the body
        length = int(self.headers['body-length'])
        body = self.rfile.read(length)

        #convert the body of the requets into a dictionary for easier handling
        incoming_dictionary = json.loads(body)
        #for debugging
        print("Incoming Dictionary: " + str(incoming_dictionary))

        #handling a registration from POST
        if path == "api/cs/login":
            print("Login API:")
            response = authenticateUser(incoming_dictionary)
        



def authenticateUser(dictionary):
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


#main function to execute and run the server
def main():
    #Server port
    port = 8000

    #Create server
    httpServer = http.server.HTTPServer(('', port), RequestListner)
    print("Request Listener is running on port", port)

    #start server, and shut it off by key interuption
    try: 
        httpServer.serve_forever()
    except KeyboardInterrupt:
        httpServer.server_close()
        print("Request handler has closed!")

if __name__ == "__main__":
    main()