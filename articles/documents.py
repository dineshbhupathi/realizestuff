# from django_elasticsearch_dsl import Document
# from django_elasticsearch_dsl.registries import registry
# from articles.models import *
# from django_elasticsearch_dsl import NestedField,fields,ObjectField
#
# es = Elasticsearch([{'host': 'localhost', 'port': '9200'}], timeout=30, max_retries=10, retry_on_timeout=True)
#
# name_analyzer = analyzer(
#     'name',
#     tokenizer = tokenizer('split_words', 'simple_pattern_split'),
#     filter = ['lowercase']
# )
#
# @registry.register_document
# class SuggetionsDocument(Document):
#     name = Text(analyzer=name_analyzer)
#     class index:
#         name = 'suggestions'
#         settings = {
#             "number_of_shards": 1,
#             "number_of_replicas": 0
#         }
#
#     class Django:
#         print('kk')
#         model = Suggestions
#
#         fields = [
#             'id','first_name','last_name','email','company','phone','message'
#         ]