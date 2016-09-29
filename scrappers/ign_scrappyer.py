#! usr/bin/python3

# MOVE MAJORITY OF CODE INTO SCRAPPER CLASS

import re
import requests as r
import dhtmlparser as d

ign_content = r.get("http://www.ign.com").content
dom = d.parseString(ign_content)

articles = dom.find("div", {"class": "listElmnt-blogItem"})
latest_reviews = dom.find("div", {"class": "column-game"})

for review in latest_reviews:
    link_review = re.search( r'<a href=[\'"]?([^\'" >]+)', str(review) )
    heading_review = re.search( r'class="game-title">(.*?)<', str(review) )
    rating_review = re.search( r'class="rating">(.*?)<', str(review) )
    if rating_review:
        print (link_review.group(0))
        print (heading_review.group(0))
        print (rating_review.group(0))

for article in articles:
    link_to = re.search( r'href=[\'"]?([^\'" >]+)', str(article) )
    heading = re.search(r'">(.*?)</a>', str(article))
    summary = re.search( r'</span>(.*?)<a', str(article) )
    comments = re.search( r'data-lf-article-id="(.*?)</span>', str(article) )
    if article:
        print (heading.group(0))
        print (summary.group(0))
        print (link_to.group(0))
        if comments:
            print (comments.group(0))

print ("all good")