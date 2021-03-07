from elasticsearch import Elasticsearch;
es = Elasticsearch()

import pandas as pd
import json

# when sheet_name=None, return a dict of dataframe
df_dict = pd.read_excel('/Users/wenbo/Desktop/test_data.xlsx', header=[0], sheet_name=None)

print(type(df_dict))
print(df_dict)

id = 0

for key in df_dict:
	json_objs = df_dict[key].to_json(orient='records', force_ascii=False) #force_ascii 解决中文乱码问题
	print (json_objs)
	json_objs = json.loads(json_objs)
	for json_obj in json_objs:
		print(json_obj)
		res = es.index(index="test-data", id=id, body=json_obj)
		id += 1
		print(res['result'])

es.indices.refresh(index="test-data")

res = es.search(index="test-data", body={"query": {"query_string": {"query" : "澳门特别行政区"}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
	print(hit)