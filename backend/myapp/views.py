from django.http import JsonResponse, HttpResponse
import os

from .models import Message


def api (request) :

    json = open (os.path.join (os.path.dirname(os.path.abspath(__file__)), "placeholder.json")).read()

    return HttpResponse (json)


def rank (request) :

	response = ""

	categories = ['Другое', 'Еда и продукты', 'Кафе, рестораны и бары', 'Одежда, обувь, аксессуары', 'Аптеки и медицина', 'Красота и парфюмерия', 'Оптика', 'Электроника', 'Авто', 'Мероприятия', 'Товары для животных', 'Спорт', 'Развлечения и хобби', 'Уход за собой', 'Услуги и сервис', 'Цветы и подарки', 'Путешествия', 'Такси и каршеринг', 'Ювелирные изделия и часы', 'Дом и ремонт', 'Товары для детей', 'Обучение', 'Книги, кино, искусство', 'Финансы', 'Софт', 'Государство', 'ЖКХ', 'События']
	for category in categories :
		objs = Message.objects.filter (category = category). order_by ("-date")
		count = 0
		for obj in objs  :
			response += obj.id + "\n"
			if count >= 5 : break
			obj.rank = count
			obj.save()
			count += 1

	return HttpResponse (response)


def getRangedmessages (type, value) :
    
    if type == "sender" :
        objs = Message.objects.filter (sender = value)
    else : 
        objs = Message.objects.filter (category = value)

    objs = objs.order_by ("-date")[0:5]

    return [obj.getObj() for obj in objs]


def test (request) :

	actual = { 
		"name" : "Актуальное", 
		"blocks" : [
			{ "name" : "События", "messages" : getRangedmessages("sender", "SmartMail Hack")}, 
			{ "name" : "Переписки", "messages" : getRangedmessages("sender", "Hackathon Data 1")}
		]
	}

	hot = {
		"name" : "Горячее",
		"blocks" : [
			{ "name" : "KUPIVIP.RU", "messages" : getRangedmessages("sender", "KUPIVIP.RU")},
			{ "name" : "Lamoda", "messages" : getRangedmessages("sender", "Lamoda")},
			{ "name" : "Top Shop", "messages" : getRangedmessages("sender", "Top Shop")},
			{ "name" : "La Redoute", "messages" : getRangedmessages("sender", "La Redoute")},
		]
	}

	mailing = [
		{ 
            "name" : "Одежда, обувь, аксессуары", 
            "blocks" : [
                { "name" : "KUPIVIP.RU", "messages" : getRangedmessages("sender", "KUPIVIP.RU")},
                { "name" : "Lamoda", "messages" : getRangedmessages("sender", "Lamoda")},
            ]
        },
        
        { 
            "name" : "Товары для детей", 
            "blocks" : [
                { "name" : "Mamsy Kids", "messages" : getRangedmessages("sender", "Mamsy Kids")},
                { "name" : "Mothercare", "messages" : getRangedmessages("sender", "Mothercare")},
            ]
        },
        
        { 
            "name" : "Другое", 
            "blocks" : [
                { "name" : "MediaMarkt", "messages" : getRangedmessages("sender", "MediaMarkt")},
                { "name" : "Комус", "messages" : getRangedmessages("sender", "Комус")},
            ]
        }
	]

	response = {
        "actual" : actual, 
        "hot" : hot, 
        "mailing" : mailing
    }

	return JsonResponse (response, safe = False)