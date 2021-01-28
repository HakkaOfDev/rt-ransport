import json

class User:
    def __init__(self, id=0, firstName="", lastName="", email="", password="", address="", tel="", admin=False) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.address = address
        self.tel = tel
        self.admin = admin
        super().__init__()


