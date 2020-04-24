# This file takes two functions in GCF, and sends a simple payload from one to the other to print a "Hello World" function.

# Function 1 - sender
import requests

def hello_world(request):
    request_json = request.get_json()
    print(request_json)
    if request_json and 'first_name' and 'last_name' in request_json:
        url = "https://us-central1-reverse-ssh-tunnels.cloudfunctions.net/sam-se-test2"
        payload = "{\n\"first_name\": \"Sam\",\n\"last_name\": \"Chapman\"\n}"
        print(payload)
        headers = {
            'Content-Type': 'application/json'
        }
        response=requests.request("POST",url, headers=headers,data = payload)
        print(response)
    else:
        return f"Hello World! But I need more info..."
 
 # Function 2- receiver
 def hello_world(request):
    request_json = request.get_json()
    print(request_json)
    if request_json and 'first_name' and 'last_name' in request_json:
        print(request_json['first_name']+ " "+ request_json['last_name'] + " says 'hello world!'")
    else:
        print("Hello World! But I need more info...")
