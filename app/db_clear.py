import requests

# base_url = "http://localhost:5000/api"
# response = requests.get(f"{base_url}/contacts")



def hard_code_clear():
    base_url = "http://127.0.0.1:5000/api"
    response = requests.get(f"{base_url}/contacts").json()
    print("here")

    for result in response:
        id = result["id"]
        x = f"{base_url}/contacts/{id}"

        response = requests.delete(x)

    print("made it here")

def repopulate():
    data = [
        {
            "address": "1 coo", 
            "email": "lacroix@can.com", 
            "id": "IgwNYxeh4-GOrDSRH_ef1gGs1MkBDoIJOZ2F1p95-NM", 
            "name": "lacroix", 
            "phone_number": "1234"
        }, 
        {
            "address": "home", 
            "email": "hi@gmail.co", 
            "id": "80h2XmBbPdLI4KtsgjYdz8IUfOk74PKzeV3ExLBDF0g", 
            "name": "me", 
            "phone_number": "4321"
        },
        {
            "address": "your backyard",
            "email": "yo@web.net",
            "id": "you'll overwrite this anyways",
            "name": "homework",
            "phone_number": "9876"
        }
    ]

    base_url = "http://127.0.0.1:5000/api"
    response = requests.get(f"{base_url}/contacts").json()

    for contact in data:
        requests.post(f"{base_url}/contacts", json=contact)
        print(requests.get(f"{base_url}/contacts"))
    
