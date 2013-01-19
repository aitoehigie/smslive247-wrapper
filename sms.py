import urllib
import urllib2

#***********************global-settings*************************
global url, owneremail, subacct, subacctpwd, sender, number_range, sessionID
url = "http://www.smslive247.com/http/index.aspx?"
owneremail="your email address registered on smslive247.com"
subacct="your smslive247.com subacct username"
subacctpwd="your smslive247.com subacct password"
sender = "display name of the sender"
supported_networks = [234708,234802,234808,234812,234705,234805,234811,234807,234815,234703,234706,234803,234806,234810,234813,234816,234809,234817,234818]
#***************************************************************#

def login(owneremail=owneremail, subacct=subacct, subacctpwd=subacctpwd):
	params = urllib.urlencode(dict(cmd="login", owneremail=owneremail, subacct=subacct, subacctpwd=subacctpwd))
	response = urllib2.urlopen(url, params)
	for item in response.readlines():
		sessionID = item[4:]
		return sessionID
	response.close()
sessionID = login()

def getacctbalance(cmd="querybalance"):
	params = urllib.urlencode(dict(cmd=cmd, sessionid=sessionID))
	response = urllib.urlopen(url, params)
	for item in response.readlines():
		return item[4:]
	response.close()

def sendmessage(message, sendto, sessionid=sessionID, sender=sender):
	if len(str(sendto)) != 13:
		return "That is not a valid Nigerian GSM number!"
	elif len(str(sendto)) == 13 and str(sendto)[0:6] in str(supported_networks):
		params = urllib.urlencode(dict(sendto=str(sendto), cmd="sendmsg", sessionid=sessionID, message=message, sender=sender))
		response = urllib2.urlopen(url, params)
		for item in response.readlines():
			return item[4:]
		response.close()
	else:
		return "You are trying to send a message to an unsupported network!"




