import urllib
import json
serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'
print "Note:('Enter -1 to exit')"
while True:
	address=raw_input('Enter the location : ')
	if address=='-1': break

	url=serviceurl+urllib.urlencode({'sensor':'false','address':address})

	print "Retriving.....",url
	uh=urllib.urlopen(url).read()

	print "Retrived",len(uh),'characters'

	try: js=json.loads(str(uh))

	except: js=None

	if 'status' not in js or js['status']!='OK':
		print "...Failed...."
		print uh
		continue

	#print json.dumps(js , indent=4)

	lat=js["results"][0]["geometry"]["location"]["lat"]
	lng=js["results"][0]["geometry"]["location"]["lng"]
	pincode=js["results"][0]["address_components"][3]["long_name"]
	print "Latitude: ",lat
	print "Longititude: ",lng
	print "pin-code: ",pincode
	location=js["results"][0]["formatted_address"]
	print location

