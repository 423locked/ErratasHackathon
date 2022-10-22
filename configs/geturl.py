from configs.hosts import *


def getUrlByConfigs():
    return f"postgres://{HOST_USER}:{HOST_PASS}@{HOST_IP}:{HOST_PORT}/{DB_NAME}"
