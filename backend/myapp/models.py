from django.db import models
import json


class Message (models.Model):

    id = models.CharField (max_length = 128, primary_key=True)
    url = models.TextField ()
    icon = models.TextField ()
    title = models.CharField (max_length = 128)
    body = models.CharField (max_length = 128)
    date = models.DateTimeField (auto_now_add = False)
    sender = models.CharField (max_length = 128, default = "")
    category = models.CharField (max_length = 128, default = "")
    rank = models.IntegerField (default = 0)


    def getObj (self) :

    	return {
		    "url" : self.url,
		    "icon" : self.icon,
		    "title" : self.title,
		    "body" : self.body,
		    "date" : self.date.strftime("%d.%m.%Y"),
            "sender" : self.sender,
            "category" : self.category,
            "rank" : self.rank,
    	}


    def __str__ (self) :

        return json.JSONEncoder().encode(self.getObj())