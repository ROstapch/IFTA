# IFTA

Before running, add 2 more files to root directory of project

*****************
- secret/my.cnf
________________


[client]
user = USER_NAME
database = DATABASE_NAME
password = USER_PASSWORD
default-character-set = utf8



*****************
- secret/mykeys.py
________________


SECRET_KEY = "secretkey"

COMPANY_API_KEYS = [
	{
		'company name' : "company api key",
	},
]
