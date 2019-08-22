from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse
import csv




'''
convert date string from yyyy-mm-dd to mm/dd/yyyy format
'''
def __convert_date(datestr):
	date = datetime.datetime.strptime(datestr, "%Y-%m-%d")
	newdate = datetime.date.strftime(date, "%m/%d/%Y")
	
	return newdate


def __convert(data):
	#synchronizing headers of EFS and KT template
	try:
		__EFS_header = data[0].split(',')
		__header = {
			"Date*" : __EFS_header.index("Tran Date"),
			"Time (UTC)*": __EFS_header.index("Tran Time") if "Tran Time" in __EFS_header else False,
			"Jurisdiction*": __EFS_header.index("State/ Prov"),
			"Driver" : __EFS_header.index("Driver Name"),
			"Vehicle*" : __EFS_header.index("Unit"),
			"Fuel Type*" : __EFS_header.index("Item"),			#check if Diesel
			"Gallons/Liters*" : __EFS_header.index("Currency"),
			"Volume*" : __EFS_header.index("Qty"),
			"USD/CAD*" : __EFS_header.index("Currency"),
			"Total Cost*" : __EFS_header.index("Amt"),
			"Vendor Name*" : __EFS_header.index("Location Name"),
			"Location" : __EFS_header.index("City"),
			"Miles/Kilometers" : "Miles",
			"Odometer" : "",
			"Reference #" : "",
			"Notes" : ""
			}
	except Exception:
		return None

	#setting up KT-alike headers for converted data file
	converted_data = []
	row_data = []
	for key in __header:
		row_data.append(key)
	converted_data.append(row_data)

	#filling in the rows for diesel type product
	for i in range(1, len(data)):
		row_data = []
		temp = data[i].split(',')
		if (len(temp) == len(__EFS_header)):
			if (temp[__header["Fuel Type*"]] == "ULSD" or temp[__header["Fuel Type*"]] == "FUEL" 
				or "DSL" in temp[__header["Fuel Type*"]]):
				row_data.append(__convert_date(temp[__header["Date*"]]))
				row_data.append(temp[__header["Time (UTC)*"]] if __header["Time (UTC)*"] else "12:00")
				row_data.append(temp[__header["Jurisdiction*"]])
				row_data.append(temp[__header["Driver"]])
				row_data.append(temp[__header["Vehicle*"]])
				row_data.append('Diesel')
				row_data.append('Gallons' if temp[__header["Gallons/Liters*"]].endswith('Gallons') else 'Liters')
				row_data.append(temp[__header["Volume*"]])
				row_data.append('USD' if temp[__header["USD/CAD*"]].startswith('USD') else 'CAD')
				row_data.append(temp[__header["Total Cost*"]])
				row_data.append(temp[__header["Vendor Name*"]])
				row_data.append(temp[__header["Location"]])
				row_data.append(__header["Miles/Kilometers"])
				row_data.append(__header["Odometer"])
				row_data.append(__header["Reference #"])
				row_data.append(__header["Notes"])

				converted_data.append(row_data)

	return (converted_data)


def EFS_to_KT_convert(csv_file):
	converted_file_name = csv_file.name[:-4] + "_converted"
	received_data = csv_file.read().decode("utf-8").split('\n')
	
	if received_data and len(received_data) > 0:
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=%s' % converted_file_name

		writer = csv.writer(response)
		converted_data = __convert(received_data)
		if converted_data:
			for row in converted_data:
				writer.writerow(row)
		else:
			return HttpResponseRedirect(reverse("Convert:upload_csv"))

		return response
	else:
		return HttpResponseRedirect(reverse("Convert:upload_csv"))
