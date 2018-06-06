from mysite.es.EsClientConnection import EsClientConnection
import pymysql.cursors
from config.es_config import index_mappings, test_mappings


def test1():
    _select_filed = "product_id,provider_id,is_published,is_deleted,created_at,updated_at,provider_code,code,subcode,name,name_provider,image_url,thumbnail_url,map_image_url,video_url,advertised_price,departure_city,return_city"
    es = EsClientConnection('127.0.0.1:9200', index_mappings)
    # 连接数据库
    connect = pymysql.Connect(
        host='192.168.100.244',
        port=3306,
        user='root',
        passwd='P0F5rNH8qBgCnWGD',
        db='tff_tour',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    totalRecordSql = "SELECT count(*) as total FROM tour_product"
    cursor.execute(totalRecordSql)
    totalRecord = cursor.fetchone()['total']

    index = 0
    while totalRecord >= index:
        sql = "select %(filed)s from tour_product limit %(index)s offset %(oset)s" % {"filed": _select_filed, "index": 100, "oset": index}
        cursor.execute(sql)
        results = cursor.fetchall()
        index = index + 100
        es.mysqlToEs(results)


def test2():
    es = EsClientConnection('127.0.0.1:9200', 'test', 'people', test_mappings)
    lists = [
        {'name': 'pl', 'age': 25, 'sex': '男'},
        {'name': 'lizuoqiang', 'age': 24, 'sex': '女'},
        {'name': 'zhaoguoyu', 'age': 26, 'sex': '男'}
    ]
    es.insertDataFrame('test', 'people', lists)
test2()