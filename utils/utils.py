import _sha256, uuid, json, time, jwt

from configs.hosts import JWT_SALT, TIME_TO_LIVE

def getTTL():
    return TIME_TO_LIVE

def generatePK():
    return uuid.uuid4().__str__()

def hash(_password):
    return _sha256.sha256(_password.encode()).hexdigest()

def getMailFromJSON(_jsonString):
    return json.load(_jsonString)['mail']

def checkInject(string):
    return "".join(string.split("'"))

def getTime():
    return str(int(time.time()))

# JWT utils
def genJWT(_username):
    return jwt.encode({"user":str(_username)},JWT_SALT, algorithm="HS256")

def decodeJWT(token):
    return jwt.decode(token, JWT_SALT, algorithms=["HS256"])