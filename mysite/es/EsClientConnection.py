# -*- coding: utf-8 -*-
from elasticsearch5 import Elasticsearch


class EsClientConnection:
    host = ''
    errorMessage = ''

    def __init__(self, host, index=None, type=None, body=None):
        '''
        创建的时候需要两个都要存在
        :param host:
        :param index:
        :param type:
        :param body:
        '''
        self.host = host
        self.conn = Elasticsearch([self.host])
        # 初始化mapping设置,即创建index
        indexExists = self.conn.indices.exists(index=index)
        typeExists = self.conn.indices.exists_type(index=index, doc_type=type)
        if body is not None:
            if indexExists is not True:
                if typeExists is not True:
                    self.conn.indices.create(index=index, body=body)
                else:
                    self.errorMessage = 'index not exists and type exists. it is not possible!'
            else:
                if typeExists is not True:
                    self.errorMessage = 'index index exists and type not exists'
                else:
                    self.errorMessage = 'index exists and type exists. you not need create it'

    def __del__(self):
        self.close()

    def check(self):
        '''
        输出当前系统的ES信息
        :return:
        '''
        return self.conn.info()

    def insertDocument(self, index, type, body, id=None):
        '''
        插入一条数据body到指定的index、指定的type下;可指定Id,若不指定,ES会自动生成
        :param index: 待插入的index值
        :param type: 待插入的type值
        :param body: 待插入的数据 -> dict型
        :param id: 自定义Id值
        :return:
        '''
        return self.conn.index(index=index, doc_type=type, body=body, id=id)

    def insertDataFrame(self, index, type, dataFrame):
        '''
        批量插入接口;
        bulk接口所要求的数据列表结构为:[{{optionType}: {Condition}}, {data}]
        其中optionType可为index、delete、update
        Condition可设置每条数据所对应的index值和type值
        data为具体要插入/更新的单条数据
        :param index: 默认插入的index值
        :param type: 默认插入的type值
        :param dataFrame: 待插入数据集
        :return:
        '''
        dataList = dataFrame.to_dict(orient='records')
        insertHeadInfoList = [{"index": {}} for i in range(len(dataList))]
        temp = [dict] * (len(dataList) * 2)
        temp[::2] = insertHeadInfoList
        temp[1::2] = dataList
        try:
            return self.conn.bulk(index=index, doc_type=type, body=temp)
        except Exception as e:
            return str(e)

    def deleteDocById(self, index, type, id):
        '''
        删除指定index、type、id对应的数据
        :param index:
        :param type:
        :param id:
        :return:
        '''
        return self.conn.delete(index=index, doc_type=type, id=id)

    def deleteDocByQuery(self, index, query, type=None):
        '''
        删除idnex下符合条件query的所有数据
        :param index:
        :param query: 满足DSL语法格式
        :param type:
        :return:
        '''
        return self.conn.delete_by_query(index=index, body=query, doc_type=type)

    def deleteAllDocByIndex(self, index, type=None):
        '''
        删除指定index下的所有数据
        :param index:
        :return:
        '''
        try:
            query = {
                'query': {
                        'match_all': {}
                    }
            }
            return self.conn.delete_by_query(index=index, body=query, doc_type=type)
        except Exception as e:
            return str(e) + ' -> ' + index

    def searchDoc(self, index=None, type=None, body=None):
        '''
        查找index下所有符合条件的数据
        :param index:
        :param type:
        :param body: 筛选语句,符合DSL语法格式
        :return:
        '''
        return self.conn.search(index=index, doc_type=type, body=body)

    def getDocById(self, index, type, id):
        '''
        获取指定index、type、id对应的数据
        :param index:
        :param type:
        :param id:
        :return:
        '''
        return self.conn.get(index=index, doc_type=type, id=id)

    def updateDocById(self, index, type, id, body=None):
        '''
        更新指定index、type、id所对应的数据
        :param index:
        :param type:
        :param id:
        :param body: 待更新的值
        :return:
        '''
        return self.conn.update(index=index, doc_type=type, id=id, body=body)


    def close(self):
     if self.conn is not None:
        try:
            self.conn.close()
        except Exception as e:
            pass
        finally:
            self.conn = None

    def mysqlToEs(self, mysqlData):
        doc = []
        for value in mysqlData:
            doc.append({"index": {}})
            doc.append(value)
        self.conn.bulk(index='product', doc_type='tour_product', body=doc)