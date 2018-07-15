import requests
import urllib
import json


file = open ("/home/ivasio/vano/ids.json", "r").read()

data = json.JSONDecoder().decode(file)

for id in data :

	# msg = Message (id = message["id"])
	req = requests.get("https://e.mail.ru/api/v1/messages/message?id=" + 
		str (id) + "&access_token=ff550413f57a731ebb618f9df7d4ac3d6d0c5fb537363830&email=smartmail_team8@mail.ru")
	req = req.json()
#	print (req["body"]["correspondents"]["from"][0]["avatars"]["default"])
	urllib.request.urlretrieve(req["body"]["correspondents"]["from"][0]["avatars"]["default"], 
		"/home/ivasio/Hacks/Mail/backend/myapp/static/pics/" + str(id) + ".jpg")

	#msg.save()
