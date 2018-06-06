# -*- coding: utf-8 -*-
from mysite.mongo.MongoClientConnection import MongoClientConnection


client = MongoClientConnection('127.0.0.1', 27017, 'test', 'people')

res1 = client.find_all()
print(res1)

condition = {
    'First Name': 'Jet'
}
dsl = {
    'Last Name': 'pl'
}
client.update_one_by_param(condition, dsl)

res2 = client.find_all()
print(res2)


