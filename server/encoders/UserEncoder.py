from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
