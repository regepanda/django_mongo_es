from django.http import HttpResponse
from mysite.es.EsClientConnection import EsClientConnection
from config.es_config import index_mappings
import json


def index(request):
    es = EsClientConnection('127.0.0.1:9200', index_mappings)
    param = request.GET
    page = int(param['num'])
    pageData = 20
    startData = (page-1) * pageData
    body1 = {
        "query": {
            "multi_match": {
                "query": "西班牙",
                "fields": ["name", "code"]
            }
        }
        # "from": startData,
        # "size": pageData
    }
    body = {
        "query": {
            "term": {
                "name": "制"
            }
        }
    }
    result = es.searchDoc('product', 'tour_product', body)
    result = result['hits']['hits']
    lists = []
    for product in result:
        lists.append(product)
    lists = json.dumps(lists)
    return HttpResponse(lists)



def detail(request, question_id):
    latestQuestionList = []
    return HttpResponse(latestQuestionList)