import requests
from time import sleep

BASE_URL: str = "https://telmunnshop.squareweb.app/api"

class CPMTooldev:

    def __init__(self, acc_access_key=None) -> None:
        self.auth_token = acc_access_key  # Store the access key if provided, or None if not

    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{BASE_URL}/account_login", data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{BASE_URL}/account_register", data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        requests.post(f"{BASE_URL}/account_delete", data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/get_data", data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/set_rank", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        response = requests.get(f"{BASE_URL}/get_key_data")
        response_decoded = response.json()
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{BASE_URL}/set_money", data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

# Example of how to use it:
acc_access_key = "your_access_key_here"
cpm = CPMTooldev(acc_access_key)

# Call any of the methods after initializing
# Example: login, get player data, etc.
