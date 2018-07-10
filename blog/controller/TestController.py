from django.http import HttpResponse
import json

def index(request):
    lists = [1, 2, 3, 4, 5, 6]
    lists = json.dumps(lists)
    return HttpResponse(list)