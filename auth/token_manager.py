import requests
def get_token():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post( "https://reqres.in/api/login", json=payload )
    return response.json()["token"]