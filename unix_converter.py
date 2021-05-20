import datetime
_name_ = 'main'
#Description of the program
_author_ = "Preston Miller & Chaplin Bryce"
_date_ = "20160401"
_version_ = "0.01"
_description_ = "Convert unix formatted timestamps seconds since epoch [1970 - 01 - 01 00:00:00]) to human readable"

def main():
	'''The main function queries the user for a unix timestamp and 
calls the unix_converter to process the input. :return:nothing.'''
 	unix_ts = int(raw_input('Unix timestamp to convert: \n>>'))
	print (unixConverter(unix_ts))

def unixComverter(timestamp):
	"""The unix_converter function uses the date time library to convert the timestamp
:param timestamp: A integer representing a unix timestamp
:return: A human readable date string """
	date_ts = datetime.datetime.utcfromtimestamp(timestamp)
	return date_ts.strftime('%m/%d/%Y/ %I:%M:%S %p UTC')

if _name_=='_main_':
	main()
