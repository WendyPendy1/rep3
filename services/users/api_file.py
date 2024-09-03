import requests

from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from config.headers import Headers
from services.users.modules.user_model import UserModel

class UsersAPI():
    def __init__(self):
        self.payloads=Payloads()
        self.endpoints=Endpoints()
        self.headers=Headers()

    def create_user(self):
        responce=requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        assert responce.status_code==200, responce.json()
        model = UserModel(**responce.json())
        return model

    def get_user_by_id(self, uuid):
        responce = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert responce.status_code == 200, responce.json()
        model = UserModel(**responce.json())
        return model
