import _sha256, uuid, json


def generatePK():
    return uuid.uuid4().__str__()


def hash(_password):
    return _sha256.sha256(_password.encode()).hexdigest()


def getMailFromJSON(_jsonString):
    return json.load(_jsonString)['mail']
