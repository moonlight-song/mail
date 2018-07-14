import json
import requests

msgList = json.loads(open('10first.json').read())
output = []

for message in msgList["messages"] :

	URL = "https://e.mail.ru/api/v1/messages/message?id=" +message["id"] + "&access_token=ff550413f57a731ebb618f9df7d4ac3d6d0c5fb537363830&email=smartmail_team8@mail.ru"

	PARAMS = {}
	r = requests.get(url = URL, params = PARAMS)
	 
	# extracting data in json format
	data = r.json()

	letterObj = {
		"priority" : data["body"]["priority"],
		"attaches" : data["body"]["attaches"],
		"date" : data["body"]["date"],
		"correspondents" : data["body"]["correspondents"],
		"meta" : data["body"]["meta"],
		"replies" : data["body"]["replies"],
		"folder" : data["body"]["folder"],
		"body" : data["body"]["body"],
		"snippet" : data["body"]["snippet"],
		"flags" : data["body"]["flags"],
		"subject" : data["body"]["subject"],
	}

	if data["body"]["transaction_category"] :
		letterObj["transaction_category"] = data["body"]["transaction_category"]
	else:
		letterObj["transaction_category"] = None
		
	output.append ()

output = json.JSONEncoder().encode(output)
outFile = open("out.json", "w")
outFile.write(output)