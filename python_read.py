import pandas as pd
import json

# when sheet_name=None, return a dict of dataframe
df_dict = pd.read_excel('/Users/wenbo/Desktop/test_data.xlsx', header=[0, 1, 2], sheet_name=None)

print(type(df_dict))
print(df_dict)

f = open("/Users/wenbo/Desktop/output.json", "w")

for key in df_dict:
	json_str = df_dict[key].to_json(orient='records', force_ascii=False) #force_ascii 解决中文乱码问题
	print (json_str)
	f.write(json.dumps(json.loads(json_str), indent=4, ensure_ascii=False)) #loads之后再dumps可以美化json
	
f.close()