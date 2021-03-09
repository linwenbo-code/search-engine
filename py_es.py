from elasticsearch import Elasticsearch;
es = Elasticsearch()

import pandas as pd
import json

# when sheet_name=None, return a dict of dataframe
# read and parse excel
df_dict = pd.read_excel('/Users/wenbolin/Desktop/test_data.xlsx', header=[0, 1, 2], sheet_name=['区直部门', '南宁市', '柳州市'])

# print out result to debug
print(type(df_dict))
print(df_dict)

id = 0

# for test: reset index in every run, ignore status code 400 (index already exists)
es.indices.delete(index="_all") # delete all indices
es.indices.create(index="test-data", ignore=400)

# feed data to elastic search at default setting localhost:9200
for key in df_dict:
	print('key is ' + key)
	json_objs = df_dict[key].to_json(orient='records', force_ascii=False) #force_ascii 解决中文乱码问题
	# json_objs from str to json objects
	json_objs = json.loads(json_objs)
	print ('excel 记录条数：' + str(len(json_objs)))
	for json_obj in json_objs:
		print(json_obj)
		print('id is ' + str(id))
		res = es.index(index="test-data", id=id, body=json_obj)
		id += 1
		# print(res['result'])

es.indices.refresh(index="test-data")

# try a search query
res = es.search(index="test-data", body={"query": {"query_string": {"query" : "澳门特别行政区"}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
	print(hit)
	
#########################################	
#http server to receive user query
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}
host = ('localhost', 8888)

class Resquest(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps(data).encode())
	def do_POST(self):
	
		# process user data
		print(self.headers)
		print(self.command)
		req_datas = self.rfile.read(int(self.headers['content-length'])) #重点在此步!
		print(req_datas.decode())
		data = {
			'result_code': '2',
			'result_desc': 'Success',
			'timestamp': '',
			'data': {'message_id': '25d55ad283aa400af464c76d713c07ad'}
		}
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		
		# do search with query user typed
		query = req_datas.decode()
		res = es.search(index="test-data", body={"query": {"query_string": {"query" : query}}})
		# 看看命中了多少次
		result = "Got %d Hits:" % res['hits']['total']['value']
		print(result)
		self.wfile.write(json.dumps(res['hits']['hits'], ensure_ascii=False).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()