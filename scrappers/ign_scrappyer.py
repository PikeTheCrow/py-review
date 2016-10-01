#! usr/bin/python3

# MOVE MAJORITY OF CODE INTO SCRAPPER CLASS
# remove if comment and nav to each page and find the comment total

import re
import requests as r
import dhtmlparser as d
import dryscrape

ign_content = r.get("http://www.ign.com").content
dom = d.parseString(ign_content)

articles = dom.find("div", {"class": "listElmnt-blogItem"})
latest_reviews = dom.find("div", {"class": "column-game"})

for review in latest_reviews:
    link_review = re.findall( r'href="(.*?)"', str(review) )
    heading_review = re.findall( r'class="game-title">(.*?)<', str(review) )
    rating_review = re.findall( r'class="rating">(.*?)<', str(review) )
    if rating_review:
        print (heading_review[0])
        print (rating_review[0])
        if link_review:
            sess = dryscrape.Session()
            sess.visit(link_review[0])
            response = sess.body()
            dom_link = d.parseString(response)
            find_comment = dom_link.find("div", {"class": "article-comments wrap"})
            for comment in find_comment:
                amount = re.findall( r'<span>(.*?)<', str(comment) )
                print (amount)
            
for article in articles:
    heading_article = re.findall( r'>(.*?)</a>\n<p>', str(article) )
    summary_article = re.findall( r'</span>(.*?)<a', str(article) )
    link_article = re.findall(r'href="(.*?)"', str(article) )
    if heading_article:
        print (heading_article[0])
        print (summary_article[0])
        print (link_article[0])

print ("all good")