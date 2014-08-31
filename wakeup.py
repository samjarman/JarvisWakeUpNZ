import urllib2
import sys
import json
import pprint
import os

METSERVICE_BASE = 'http://metservice.com/publicData/'

def get_response(url):
	try:
		response = urllib2.urlopen(url)
	except urllib2.HTTPError:
		return None
	return json.loads(response.read())

if __name__ == '__main__':
	try:
		city = sys.argv[1]
	except IndexError:
		city = 'christchurch'
		
	url = ''.join([METSERVICE_BASE, "localForecast", city])
	print url
	resp = get_response(url)
	#print(resp)
	s = "Good Morning, sir. The day is %s. The forecast in %s is %s with a high of %s." % ( resp['days'][0]['riseSet']['day'],
										resp['locationIPS'], 
										resp['days'][0]['forecast'],
										resp['days'][0]['max'])
	#print(resp['locationIPS'])
	#print(resp['forecast'])
	print(s)
	os.system('say %s' % (s))

