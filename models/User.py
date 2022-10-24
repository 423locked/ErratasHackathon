import json


class User:
    def __init__(self, _firstname, _middlename, _lastname, _groupname, _username, _password, _mail, _phone):
        self.firstname = _firstname
        self.middlename = _middlename
        self.lastname = _lastname
        self.groupname = _groupname
        self.username = _username
        self.password = _password
        self.identifier = json.dumps({'mail': _mail, 'phone': _phone})

    def __str__(self):
        return 'User({}, {}, {}, {}, {}, {}, {})'\
            .format(self.username, self.password, self.name, self.surname)
