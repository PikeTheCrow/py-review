#! usr/bin/python3

# MOVE MAJORITY OF CODE INTO SCRAPPER CLASS

import re
import requests as r
import dhtmlparser as d

gamespot_content = r.get("http://www.gamespot.com").content
dom = d.parseString(gamespot_content)

articles = dom.find("article", {"class": "media media-article"})

for article in articles:
    titles = re.findall( r'<h3 class="media-title">(.*?)</h3>', str(article) )
    content = re.findall( r'<p class="media-deck">(.*?)</p>', str(article) )
    link_to = re.findall( r'<a class="js-event-tracking" href="(.*?)" data-event-tracking', str(article) )
    if titles:
        print (titles)
        print (content)
        print (link_to)