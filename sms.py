#!/usr/bin/env python

#**************************************************************************************
"""
description= Python HTTP API wrapper for smslive247.com
author=Pystar
author_email=aitoehigie@gmail.com.
Date=2013
Revised: 18/06/2014
"""

import requests

#***********************global-settings*************************
global url, owneremail, subacct, subacctpwd, sender, number_range, sessionID
url = "http://www.smslive247.com/http/index.aspx?"
owneremail="your email address registered on smslive247.com"
subacct="your smslive247.com subacct username"
subacctpwd="your smslive247.com subacct password"
sender = "display name of the sender"
supported_networks = [234708,234802,234808,234812,234705,234805,234811,234807,234815,234703,234706,234803,234806,234810,
234813,234816,234809,234817,234818]
#****************************************************************

def login(owneremail=owneremail, subacct=subacct, subacctpwd=subacctpwd):
	payload = dict(cmd="login", owneremail=owneremail, subacct=subacct, subacctpwd=subacctpwd)
	global sessionID
	sessionID = requests.post(url, data=payload).text[4:]
	return sessionID

def getacctbalance(cmd="querybalance"):
	payload = dict(cmd=cmd, sessionid=sessionID)
	response = requests.post(url, data=payload)
	return response.text[4:]

def sendmessage(message, sendto, sessionid=sessionID, sender=sender):
	if len(str(sendto)) != 13:
		return "That is not a valid Nigerian GSM number!"
	elif len(str(sendto)) == 13 and str(sendto)[0:6] in str(supported_networks):
		payload = dict(sendto=str(sendto), cmd="sendmsg", sessionid=sessionID, message=message, sender=sender)
		response = requests.post(url, data=payload).text[4:]
		return response
	else:
		return "You are trying to send a message to an unsupported network!"


if __name__ == "__main__":
	sessionID = login(owneremail=owneremail, subacct=subacct, subacctpwd=subacctpwd)



