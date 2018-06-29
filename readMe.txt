[django命令工具]
    django-admin startproject mysite 【创建项目】
    python manage.py migrate 【初始化数据库】

    python manage.py startapp blog 【创建一个应用】
    python manage.py makemigrations polls 【包含新创建的应用对应数据库的迁移文件】
    python manage.py migrate polls 【执行这些迁移文件】

    python manage.py runserver 【启动服务】


[elasticsearch python操作语法]
    [单一操作]
        [插入]
            body = {"name": 'lucy', 'sex': 'female', 'age': 10}
            es = Elasticsearch(['localhost:9200'])
            es.index(index='indexName', doc_type='typeName', body, id=None)
        [删除]
            es.delete(index='indexName', doc_type='typeName', id='idValue')
        [指定查找]
            es.get(index='indexName', doc_type='typeName', id='idValue')
        [更新]
            es.update(index='indexName', doc_type='typeName', id='idValue', body={待更新字段})
    [批量操作]
        [条件查询]
            query = {'query': {'match_all': {}}}# 查找所有文档
            query = {'query': {'term': {'name': 'jack'}}}# 查找名字叫做jack的所有文档
            query = {'query': {'range': {'age': {'gt': 11}}}}# 查找年龄大于11的所有文档
            allDoc = es.search(index='indexName', doc_type='typeName', body=query)
            print allDoc['hits']['hits'][0]# 返回第一个文档的内容
        [条件删除]
            query = {'query': {'match': {'sex': 'famale'}}}# 删除性别为女性的所有文档
            query = {'query': {'range': {'age': {'lt': 11}}}}# 删除年龄小于11的所有文档
            es.delete_by_query(index='indexName', body=query, doc_type='typeName')
        [条件更新]
            update_by_query：更新满足条件的所有数据，写法同上删除和查询


