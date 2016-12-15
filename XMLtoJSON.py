#!/usr/bin/env python
import xml.etree.cElementTree as ET
import pprint
import re
import json


problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

#CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {}
    addr={}
    nodes_refs=[]
    if element.tag == "node" or element.tag == "way" :
        node['type']=element.tag
        node['id']=element.attrib['id']
        try:
            node['visible']=element.attrib['visible']
        except KeyError:
            pass
        node['created']={
          "version":element.attrib['version'],
          "changeset":element.attrib['changeset'],
          "timestamp":element.attrib['timestamp'],
          "user":element.attrib['user'],
          "uid":element.attrib['uid']
        }
        try:
            node['pos']=[float(element.attrib['lat']), float(element.attrib['lon'])]
        except KeyError:
            pass
        addr={}
        for tag in element.iter("tag"):
            if problemchars.match(tag.attrib['k']):
                continue
            elif "addr:" in tag.attrib['k']:
                address=tag.attrib['k']
                if ':' in address[5:]:
                    continue
                else:
                    addr[address[5:]]=tag.attrib['v']
                    
            else:
                node[tag.attrib['k']]=tag.attrib['v']
        
        if addr!={}:
            node['address']={}
            node['address']=addr
        
        for nd in element.iter('nd'):
            nodes_refs.append(nd.attrib['ref'])
        if nodes_refs!=[]:
            node['node_refs']=nodes_refs
        #print node
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    nodes_out = "aarhus_nodes.json"
    ways_out = "aarhus_ways.json"
    with open(nodes_out, "w") as nfo, open(ways_out,"w") as wfo:
        for _, element in ET.iterparse(file_in):
            el={}
            el = shape_element(element)
            if el and el['type']=="node":
                if pretty:
                    nfo.write(json.dumps(el, indent=2)+"\n")
                else:
                    nfo.write(json.dumps(el) + "\n")
            if el and el['type']=="way":
                if pretty:
                    wfo.write(json.dumps(el, indent=2)+"\n")
                else:
                    wfo.write(json.dumps(el) + "\n")

process_map("aarhus_denmark.osm")