from data.User import User
from services.Service import Service


class UserService(Service):

    def __init__(self) -> None:
        super().__init__()

    def findAll(self):
        users = []
        rows = self.sql.getRows('SELECT * FROM users')
        for user in rows:
            users.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7]))
        return users
