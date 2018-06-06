from django.http import HttpResponse
from mysite.es.EsClientConnection import EsClientConnection
from config.es_config import index_mappings
import json
import types


def index(request):
    es = EsClientConnection('127.0.0.1:9200', 'product', 'tour_product', index_mappings)
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


def classToDict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict