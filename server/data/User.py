class User:
    def __init__(self, id=0, first_name="", last_name="", email="", password="", address="", tel="", admin=False) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address
        self.tel = tel
        self.admin = admin
        super().__init__()


