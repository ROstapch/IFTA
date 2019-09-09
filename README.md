# IFTA

To run this project create 2 files:
- secret/my.cnf
*****************
[client]
user = USER_NAME
database = DATABASE_NAME
password = USER_PASSWORD
default-character-set = utf8


- secret/mykeys.py
*****************
SECRET_KEY = "secretkey"

COMPANY_API_KEYS = [
	{
		'company name' : "company api key",
	},
]
