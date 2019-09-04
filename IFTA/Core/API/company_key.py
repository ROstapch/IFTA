from django.conf import settings

def key_by_name(company_name):
	key = None
	try:
		for company in settings.COMPANY_API_KEYS:
			if company_name in company:
				key = company[company_name]
		key_header = {"X-Api-Key" : key}
		return key_header
	except Exception:
		return None


def companies():
	company_list = []
	try:
		for company in settings.COMPANY_API_KEYS:
			company_list.append(list(company.keys())[0])
		return company_list
	except Exception:
		return None
