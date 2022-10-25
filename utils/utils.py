import _sha256, uuid, json, time, jwt

from configs.hosts import JWT_SALT


def generatePK():
    return uuid.uuid4().__str__()


def hash(_password):
    return _sha256.sha256(_password.encode()).hexdigest()


def getMailFromJSON(_jsonString):
    return json.load(_jsonString)['mail']

def checkInject(string):
    return "".join(string.split("'"))

def genJWT():
    return jwt.encode({"unic":str(time.time())},JWT_SALT, algorithm="HS256")