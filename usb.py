"""
USB Vendor ID and Product ID Lookup Program v.1.0
Online Tool

"""


import urllib2
import sys

def main():
	"""
	The main function opens the url and parse the file before
	searching for the user supplied vendor and product IDS
	:return:nothing
	
	"""
	url = 'http://www.linux-usb.org/usb.ids'
	usbs = {}
	
	#url open function creates a file-like object and can be treated similarly
	
	usb_file = urllib2.urlopen(url)
	
	#The curr_id variable is used to keep track of the current vendor being
	#process in to the dictionary.
	
	curr_id = ''
	
	for line in usb_file:
		#Any commented line or blank line should be skipped.
		if line.startswith('#') or line == '\n':
			pass
			
		else:
			#Lines that are not tabbed are vendor lines.
			if not(line.startswith('\t')) and (line[0].isdigit() or line[0].islower()):
				#Call the getRecord helper function to parse the vendor ID and Name.
				id,name = getRecord(line.strip())
				curr_id = id
				usbs[id] = [name,{}]
				
				#Lines with one tab are product lines
				
			elif line.startswith('\t') and line.count('\t') == 1:
				#Call the getRecord helper function to parse the
				#product ID and Name
				id, name = getRecord(line.strip())
				usbs[curr_id][1][id] = name
				
	#pass the usbs dictionary and search for the supplied vendor
	#and product id match.			
	searchKey(usbs)
				
def getRecord(record_line):
	"""
	The getRecord function split the ID and Name on each line.
	:param record_line: The current line in the USB file
	:return: record_id and record_name from the USB file
	"""
	
	#Find the first instance of a space  -- should be right after the id.
	split = record_line.find(' ')
	
	#Use string slicing to split the string in two at the space
	record_id = record_line[:split]
	record_name = record_line[split + 1:]
	return record_id, record_name
	
def searchKey(usb_dict):
	"""
	The search_key function looks for the user supplied vendor and
	product IDs against the USB dictionary that was parsed in the
	main and getRecord functions.
	
	:param usb_dict: The dictionary containing our list of vendors and
	products to query against.
	:return: Nothing
	"""
	
	#accepts user arguments for vendor and product id. Error will be
	#thrown if there are less than 2 supplied arguments. Any additional 
	#arguments will be ignored.
	
	try:
		vendor_key = sys.argv[1]
		product_key = sys.argv[2]
	except IndexError:
		print 'Please provide the vendor id and product id seperated by spaces.'
		sys.exit[1]
		
	#Search for the vendor Name by looking for the Vendor ID key
	#in usb_dict. The zeroth indexof the list is the Vendor Name. If Vendor id
	#is not found , exit the program.
	
	try:
		vendor = usb_dict[vendor_key][0]
	
	except KeyError:
		print 'Vendor ID not found.'
		sys.exit(0)
		
	#Search for the Product Name by looking in the product dictionary
	#in the first index of the list. If the Product ID is not found  print
	#the vendor Name as a partialmatch and exit.
	
	try:
		product = usb_dict[vendor_key][1][product_key]
	
	except KeyError:
		print 'Vendor: {}\nProduct ID not found.'.format(vendor)
		sys.exit(0)
		
	#If both the Vendor and Product IDs are found, print their
	#respective names to the console.
	print 'Vendor: {}\nProduct: {}'.format(vendor, product)

main()
