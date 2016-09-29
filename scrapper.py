#! usr/bin/python3

import requests as r
import dhtmlparser as d

ign_content = r.get("http://www.ign.com").content

dom = d.parseString(ign_content)

content = dom.find("div", {"class": "listElmnt-blogItem"})
top_games_ign = dom.find("div", {"class": "topgames-module"})

#print (content)
print (top_games_ign)
print ("all good")