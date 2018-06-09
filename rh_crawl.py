from requests_html import HTMLSession
from functools import reduce
import json

# make web elements to python objects
def el_to_text(els,atr):
    if (atr == "absolute_links" or atr == "links"):
        return list(map(lambda el:getattr(el,atr).pop(),els))
    else:
        return list(map(lambda el:getattr(el,atr),els))

def els_to_text(el_list,atr):
    return list(map(lambda el:el_to_text(el,atr),el_list))

def els_to_items(kwargs): # {"text":[titles,firms],"links":[]}
    results = []
    for key, value in kwargs.items():
        results.append(els_to_text(value,key))
    return list(zip(*reduce(lambda x,y:x+y, results)))

def to_obj(namelist,arrays):
    result = []
    for array in arrays:
        dic = dict.fromkeys(namelist)
        for index,val in enumerate(namelist):
            dic[val] = array[index]
        result.append(dic)
    return result

def make_obj(namelist,item_dic):
    arrays = els_to_items(item_dic)
    return to_obj(namelist,arrays)
