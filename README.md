
# search-engine


人生中第一个搜索引擎
简易，却不简单
集成了elastic search
站在巨人的肩膀上，感谢老婆的支持

实现了从excel表格读取数据并feed到elastic search里面

感谢python，es的作者。

感谢卡拉先生的搜索引擎启蒙，虽然我们并未谋面


# tech stacks
1. python for 
1.1 data retrieving from excel file 
1.2 feed to elasticsearch
1.3 host http server for query requests
2. vue for 
2.1 receive user input
2.2 display query results

# prerequisite
1. excel需要全部清除下拉列表
2. wps -> 全选 -> 数据 -> 插入列表 -> 全部清除

# 经验
1. es会模糊搜索，比如搜索“澳门”，只有一个“门”字匹配的项也会显示

# steps to set up
1. install elasticsearch
2. start elasticsearch with default settting, it will serve @ localhost:9200
3. install elasticsearch lib using "pip3 install elasticsearch && pip3 install numpy && pip3 install pandas"
4. change py_es.py specifying data location
5. run py_es.py with command: python3 py_es.py
