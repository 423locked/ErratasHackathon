import uuid


def generatePK():
    return uuid.uuid4().__str__()
