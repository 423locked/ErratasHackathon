import datetime

LOGER_FILE = "./log/server.log"

def logRegister(_username):
	logFile = open(LOGER_FILE,"a")
	logFile.write(f"REGISTRATION : {_username} {datetime.datetime.now()}\n")
	logFile.close()

def logRefreshToken(_username):
	logFile = open(LOGER_FILE,"a")
	logFile.write(f"REFRESH TOKEN : {_username} {datetime.datetime.now()}\n")
	logFile.close()


def logCreateToken(_username):
	logFile = open(LOGER_FILE,"a")
	logFile.write(f"CREATE TOKEN : {_username} {datetime.datetime.now()}\n")
	logFile.close()
	
