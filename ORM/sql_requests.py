from sqlalchemy import create_engine

from configs.hosts import *

host_url = f"postgers://{HOST_USER}:{HOST_PASS}@{HOST_IP}:{HOST_PORT}/{DB_NAME}"

class SQLrequest:
	@staticmethod
	def register_user():
		pass