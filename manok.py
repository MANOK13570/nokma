import requests
from time import sleep

BASE_URL: str = "https://telmunnshop.squareweb.app/api"

class CPMTooldev:

    def __init__(self) -> None:
        self.auth_token = None

    def login(self, email, password, access_key) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": access_key }
        response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password, access_key) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": access_key }
        response = requests.post(f"{BASE_URL}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self, access_key):
        payload = { "account_auth": self.auth_token }
        params = { "key": access_key }
        requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)

    def get_player_data(self, access_key) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": access_key }
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self, access_key) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": access_key }
        response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_key_data(self, access_key) -> any:
        params = { "key": access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_money(self, amount, access_key) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": access_key }
        response = requests.post(f"{BASE_URL}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
