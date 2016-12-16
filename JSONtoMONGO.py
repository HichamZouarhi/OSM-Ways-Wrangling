#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.DAND3

Cities_Postcodes={
"Aarhus C":8000,# "Århus C"   
"Aarhus N":8200,# "Århus N"
"Aarhus V":8210,# "Århus V"
u"Åbyhøj":8230,	
"Beder":8330,	
"Brabrand":8220,	
u"Egå":8250, 
"Harlev J":8462,	
"Hasselager":8361,	
u"Hjortshøj":8530,	
u"Højbjerg":8270,	
"Lystrup":8520,	
"Malling":8340,	
u"Mårslet":8320,	
"Risskov":8240,	
"Sabro":8471,
u"Skødstrup":8541,	
"Solbjerg":8355,	
"Tilst":8381,	
"Tranbjerg":8310,# "Tranbjerg" 
"Trige":8380,	
"Viby":8260,#	"Viby"
"Hinnerup":8382,# "Søften"
"Knebel":8420,
u"Hørning":8362
}

Cities={
	u"Århus C":"Aarhus C",
	u"Århus N":"Aarhus N",
	u"Århus V":"Aarhus V",
	"Tranbjerg J":"Tranbjerg",
	"Viby J":"Viby",
	u"Søften":"Hinnerup"
}


def Insert_cleaned_data(filename,collection):
	with open(filename) as f:
		for line in f:
			data={}
			data = json.loads(line)
			try:
				address=data['address']
				if address['city'] in Cities.keys():
					address['city']=Cities[address['city']]
				if address['city'] in Cities_Postcodes.keys():
					if address['postcode']==str(Cities_Postcodes[address['city']]):
						pass
					else:
					   	address['postcode']=Cities_Postcodes[address['city']]
						data['address']=address
			except KeyError:
				pass
			#pprint(data)
			collection.insert(data)

Insert_cleaned_data("aarhus_nodes.json",db.aarhus_nodes)
Insert_cleaned_data("aarhus_ways.json",db.aarhus_ways)