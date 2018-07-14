import json
import requests


output = []

for i in range (5) :

	URL = "https://e.mail.ru/api/v1/messages/status?folder=0&limit=200&offset=" + str (200*i) + "&access_token=ff550413f57a731ebb618f9df7d4ac3d6d0c5fb537363830&email=smartmail_team8@mail.ru"
	PARAMS = {}
	r = requests.get(url = URL, params = PARAMS)
	 
	# extracting data in json format
	msgList = r.json()


	for message in msgList["body"]["messages"] :

		URL = "https://e.mail.ru/api/v1/messages/message?id=" +message["id"] + "&access_token=ff550413f57a731ebb618f9df7d4ac3d6d0c5fb537363830&email=smartmail_team8@mail.ru"

		PARAMS = {}
		r = requests.get(url = URL, params = PARAMS)
		 
		# extracting data in json format
		data = r.json()

		letterObj = {
			"id" : data["body"]["id"],
			"priority" : data["body"]["priority"],
			"attaches" : [],
			"date" : data["body"]["date"],
			"body_html" : data["body"]["body"]["html"],
			"body_text" : data["body"]["body"]["text"],
			"snippet" : data["body"]["snippet"],
			"flags" : data["body"]["flags"],
			"subject" : data["body"]["subject"],
			"correspondents_from_email" : data["body"]["correspondents"]["from"][0]["email"],
			"correspondents_from_name" : data["body"]["correspondents"]["from"][0]["name"],
			

		}
		for attach in data["body"]["attaches"]["list"] :
			letterObj["attaches"].append (attach["content_type"])

		if "transaction_category" in data["body"] :
			letterObj["transaction_category"] = data["body"]["transaction_category"]
		else:
			letterObj["transaction_category"] = None

		if len(data["body"]["correspondents"]["to"]) :
			letterObj["correspondents_to_email"] : data["body"]["correspondents"]["to"][0]["email"]
			letterObj["correspondents_to_name"] : data["body"]["correspondents"]["to"][0]["name"]
		else :
			letterObj["correspondents_to_email"] = None
			letterObj["correspondents_to_name"] = None

		output.append (letterObj)
		


output = json.JSONEncoder().encode(output)
outFile = open("out2.json", "w")
outFile.write(output)