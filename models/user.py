class User:
    def __init__(self, username=None, password=None, name=None, surname=None):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Book({}, {}, {}, {})'\
            .format(self.username, self.password, self.name, self.surname)
