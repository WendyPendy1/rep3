from services.users.api_file import UsersAPI

class BaseTest:
    def setup_method(self):
        self.api_users = UsersAPI()
