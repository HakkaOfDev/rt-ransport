from data.User import User
from services.Service import Service


class UserService(Service):

    def __init__(self) -> None:
        super().__init__()

    def findAll(self):
        users = []
        rows = self.sql.getRows('SELECT * FROM users')
        if rows != None:
            for user in rows:
                users.append(User(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7]))
            return users

    def getUserByEmail(self, email):
        print(email)
        row = self.sql.get("SELECT * FROM users WHERE email=%s", (email,))
        print(row)
        user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return user

    def ifUserExists(self, user):
        return self.sql.ifPresent("SELECT * FROM users WHERE email=%s AND first_name=%s AND last_name=%s",
                                  (user.email, user.first_name, user.last_name))

    def ifUserExistsWithEmail(self, email):
        return self.sql.ifPresent("SELECT * FROM users WHERE email=%s", (email,))

    def registerNewUser(self, user):
        self.sql.update(
            "INSERT INTO users (first_name, last_name, email, password, address, tel, admin) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user.first_name, user.last_name, user.email, user.password, user.address, user.tel, user.admin))

    def loginUser(self, email, password):
        user = self.getUserByEmail(email)
        if password == user.password:
            return True
        else:
            return False
