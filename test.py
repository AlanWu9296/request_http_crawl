#%% initialize the request
from requests_html import HTMLSession
from functools import reduce
import json
import rh_crawl as rh_crawl

session = HTMLSession()
r = session.get('https://archinect.com/jobs')

#%%
titles = r.html.xpath("//div[@class='Col1']/h1")
firms = r.html.xpath("//div[@class='Col1']/h2")
types = r.html.xpath("//div[@class='Col1']/h3")
locations = r.html.xpath("//div[@class='Col2']/p")
post_times = r.html.xpath("//div[@class='Col2']/span")
links = r.html.xpath("//li[@class='Entry ']/a")
item_name = ['title','firm','type','location','post_time','link']
el_dic = {'text':[titles,firms,types,locations,post_times],'absolute_links':[links]}


#%%

r1 = rh_crawl.make_obj(item_name,el_dic)
r1


with open('result.json','w') as f:
    f.write(json.dumps(r1))
