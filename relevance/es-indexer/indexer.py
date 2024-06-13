import csv
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# Elasticsearch에 인덱스를 생성하고 매핑 설정
def create_index(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body={
            "settings": {
                "analysis": {
                    "analyzer": {
                        "korean": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "text", "analyzer": "korean"},
                    "author": {"type": "text", "analyzer": "korean"},
                    "genre": {"type": "text", "analyzer": "korean"},
                    "description": {"type": "text", "analyzer": "korean"},
                    "rating": {"type": "float"},
                    "date": {"type": "date", "format": "yyyy.MM.dd HH:mm || yyyy.MM.dd"},
                    "completed": {"type": "boolean"},
                    "age": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "free": {"type": "boolean"},
                    "link": {"type": "keyword"}
                }
            }
        })
    else: 
        print(f'Index "{index_name}" already exists.') 

# CSV 파일에서 데이터를 읽어 Elasticsearch에 색인
def index_data():
    with open('../data/naver.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'completed' in row:
                row['completed'] = True if row['completed'].lower() in ['true'] else False
            if 'free' in row:
                row['free'] = True if row['free'].lower() in ['true'] else False
            es.index(index='naver_webtoons', body=row)

def delete_index(index_name):
    es.indices.delete(index=index_name, ignore=[400, 404])

delete_index('naver_webtoons')
create_index('naver_webtoons')
index_data()
