import requests

def client():
    credentials = {
        "username": "admin",
        "password": 1111,
    }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
                             data=credentials)

    response = requests.get("http://127.0.0.1:8000/api/users/profiles-auth/login/")


    print("Status Code: ", response.status_code)

    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()
