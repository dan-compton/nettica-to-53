import csv
import re
from BeautifulSoup import BeautifulSoup
from subprocess import call

def addAllZones(all_data):
	for row in all_data:
		call(['cli53', 'create', row[0], '--comment', row[2]])

def delAllRecords(all_data):
	for row in all_data:
		call(['cli53', 'rrpurge', row[0], '--confirm'])
		call(['cli53', 'delete', row[0]])

def cli53ARecords(all_data):
	for row in all_data:
		if len(row[3]) > 0:
			call(['cli53', 'rrcreate', row[0], '', 'A', row[3], '--ttl', '600'])

def cli53DELWWWARecords(all_data):
	for row in all_data:
		if len(row[3]) > 0:
			call(['cli53', 'rrdelete', row[0], 'www', 'A'])

def cli53MXRecords(all_data):
	for row in all_data:
		call(['cli53', 'rrcreate', row[0], '', 'MX', '10 ' + row[1], '20 ' + row[2],  '--ttl', '600'])

def cli53TXTRecords(all_data):
	for row in all_data:
		call(['cli53', 'rrcreate', row[0], '', 'TXT', "v=spf1 a mx ptr include:spf.ess.barracudanetworks.com ip4:69.46.0.121 ip4:174.121.232.154 ~all"])

def cli53CNAMERecords(all_data):
	for row in all_data:
		if len(row[4]) > 0:
			#call(['cli53', 'rrcreate', row[0], 'webmail', 'CNAME', 'mail.'+row[0], '--ttl', '600'])
			call(['cli53', 'rrcreate', row[0], 'www', 'CNAME', row[0], '--ttl', '600'])

def cliCommerceNetworksHostingRecords():
    ## REDACTED
    return
def readBarracudaCSV(f):
	#  read the csv file and populate the arrays
	all_data = []
	with open(f, 'rb') as csvfile:
		data = csv.reader(csvfile)
		# get the labels
		for row in data:
			if row[1].find(" (") > 0:
				row[1] = row[1][0:row[1].find(" ")]
			all_data.append(row[1:5])
	return all_data



def readCSV(f):
	#  read the csv file and populate the arrays
	all_data = []
	with open(f, 'rb') as csvfile:
		data = csv.reader(csvfile)

		# get the labels
		for row in data:
			# Add in the A Record information
			zone_info = row[2]
			A = ''
			MAIL = ''
            ## REDACTED
            row.append(A)
			row.append(MAIL)
			all_data.append(row)
	return all_data

if __name__ == '__main__':
	all_data = readCSV('ExportDns.csv')
	#all_data = readBarracudaCSV('barracuda.csv')

	#cli53TXTRecords(all_data)
	#cli53ARecords(all_data)
	#cli53CNAMERecords(all_data)
	#cli53MXRecords(all_data)
	#cliCommerceNetworksHostingRecords()
	#cli53DELWWWARecords(all_data)
	#delAllRecords(all_data)
	#addAllZones(all_data)

