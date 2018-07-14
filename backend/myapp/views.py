from django.http import JsonResponse, HttpResponse
#from .models import Message


def api (request) :

    json = open ("placeholder.json").read()

    return HttpResponse (json)