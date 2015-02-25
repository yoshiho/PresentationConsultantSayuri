# -*- coding: utf-8 -*-
__author__ = 'yoshiho'
import redis
import sys
from ast import literal_eval
import os
from statistics import mean

max_learn_data=100
print(os.getcwd())
r= redis.Redis(host="127.0.0.1",port=6379,db=0)
print(r.keys())
i=0
open_data=[]
store_keys=["y","speed","sentenceSpeed","parts_speed","message","interval","sentenceCount","parts","characters"]
parts_keys=["名詞", "動詞", "形容詞", "副詞", "助詞", "接続詞", "助動詞", "連体詞", "感動詞"]

while i<max_learn_data:
    file_name="15s_learning_data_"+str(i+1)
    open_data.append(r.lrange(file_name,0,-1))
    i+=1

j=0
k=0

for s in open_data:
    for p in s:

        print(open_data[j][k].decode("utf-8"))
        open_data[j][k]=literal_eval(open_data[j][k].decode("utf-8"))
        k+=1
    k=0
    j+=1

aggregated = []
for s in open_data:
    print(s)
    dic={}
    for key in store_keys:
        if(key=="parts_speed"):
            for pkey in parts_keys:
                dic[pkey] = ",".join([str(p[key][pkey]) for p in s])
        dic[key] = ",".join([str(p[key]) for p in s])
    aggregated.append(dic)

store_keys[3:3]=parts_keys

print(store_keys)
# write to file
path = os.path.join(os.path.dirname(__file__), "./learningData.txt")

with open(path, "wb") as outfile:
    line = "\t".join([str(v) for v in store_keys])
    outfile.write(line.encode("utf-8"))
    for a in aggregated:
        print(a)
        line ="\n" + "\t".join([str(a[v]) for v in store_keys])
        outfile.write(line.encode("utf-8"))
