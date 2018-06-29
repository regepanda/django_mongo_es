# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId
import syslog


class MongoClientConnection(object):
    def __init__(self, ip='127.0.0.1', port=27017, db='test', collection='people'):
        """Init MongoDB Option.
            wait more option added.
        """
        self.ip = ip
        self.port = port

        try:
            self.client = MongoClient(self.ip, self.port)
            self.db = self.client[db]
            self.collection = self.db[collection]
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient Connect failed :  " + str(e))

    def format_id(self, object_id):
        """
            Format Id.
            return a dict.
        """
        return {'_id': ObjectId(object_id)}

    def insert_one(self, document):
        """
            Insert One Document To MongoDB.
            document must be a dict.
            return a dict with document's inserted_id or False when Error occured
        """
        if not isinstance(document, dict):
            raise TypeError
        try:
            return self.collection.insert_one(document).inserted_id
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient Insert_one {document} failed:".format(document=document) + str(e))
            return False

    def insert_many(self, documents):
        """
            Insert Many Documents To MongoDB.
            documents must be a list.
            eveny document must be a dict.
            return a list with documents's inserted_ids or False when Error occured
        """
        if not isinstance(documents, list):
            raise TypeError
        for document in documents:
            if not isinstance(document, dict):
                raise TypeError
        try:
            return self.collection.insert_many(documents).inserted_ids
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient insert_many {document} failed:".format(document=document) + str(e))
            return False

    def find_one_by_id(self, object_id):
        """
            Find Result By Object_id.
            Return a dict with a document
        """
        if not isinstance(object_id, str):
            raise TypeError
        try:
            return self.collection.find_one(self.format_id(object_id))

        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient find_by_id {id} failed:".format(id=object_id) + str(e))
            return False

    def find_one_by_param(self, condition):
        """
            Find Document By Object_id.
            return a dict with a document
        """
        if not isinstance(condition, dict):
            raise TypeError
        try:
            return self.collection.find_one(condition)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient find_by_param {condition} failed:".format(condition=condition) + str(e))
            return False

    def find_many_by_param(self, condition):
        """
            Find Document By Object_id.
            return a cursor object with a or many document
        """
        if not isinstance(condition, dict):
            raise TypeError
        try:
            return self.collection.find(condition)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient find_by_param {condition} failed:".format(condition=condition) + str(e))
            return False

    def update_one_by_id(self, object_id, condition):
        """
            Update Document By Object_id.
            Return True or False
        """
        if not isinstance(condition, dict):
            raise TypeError

        try:
            self.collection.update_one(self.format_id(object_id), {"$set": condition}, upsert=False)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient update_one_by_id failed:" + str(e))
            return False
        else:
            return True

    def update_one_by_param(self, condition, kws):
        """
            Update Document By Object_id.
            Return True or False
        """
        if not isinstance(condition, dict) or not isinstance(kws, dict):
            raise TypeError
        try:
            self.collection.update_one(condition, {"$set": kws}, upsert=False)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient update_one_by_param  failed:" + str(e))
            return False
        else:
            return True

    def update_many_by_param(self, condition, kws):
        """
            Update Document By Object_id.
            Return True or False
        """
        if not isinstance(condition, dict) or not isinstance(kws, dict):
            raise TypeError
        try:
            self.collection.update_many(condition, {"$set": kws}, upsert=False)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient update_many_by_param  failed:" + str(e))
            return False
        else:
            return True

    def remove_all(self):
        """
            Remove all documents from a collection .
            Return True or False
        """
        try:
            self.collection.remove()
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient remove_all  failed:" + str(e))
            return False
        else:
            return True

    def remove_documents(self, condition):
        """
            Remove some documents from a collection .
            Return True or False
        """
        if not isinstance(condition, dict):
            raise TypeError
        try:
            self.collection.remove(condition)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient remove_documents  failed:" + str(e))
            return False
        else:
            return True

    def find_all(self):
        try:
            return self.collection.find_one()
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "MongoClient find all failed:" + str(e))
            return False