#!/usr/bin/env python
import json
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.DAND3

with open('aarhus_ways.json') as f:
	for line in f:
		data={}
		#data = json.loads(json.dumps(line))
		#pprint(json.loads(line))
		data=json.loads(line)
		#pprint(data)
		db.aarhus_ways.insert(data)

with open('aarhus_nodes.json') as f:
	for line in f:
		data={}
		#data = json.loads(json.dumps(line))
		#pprint(json.loads(line))
		data=json.loads(line)
		#pprint(data)
		db.aarhus_nodes.insert(data)