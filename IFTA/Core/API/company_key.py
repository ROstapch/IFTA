from django.conf import settings

def key_by_name(company_name):
	key = None
	for company in settings.COMPANY_API_KEYS:
		if company_name in company:
			key = company[company_name]
	key_header = {"X-Api-Key" : key}
	return key_header