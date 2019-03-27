import scraperwiki
import lxml.html
html= scraperwiki.scrape("http://www.alva.org.uk/details.cfm?p=423")

root=lxml.html.fromstring(html)
museums=root.cssselect("div table tbody")
record={}
for museumtable in museums:
         finallist=musemtable.text_content()
         print(finallist.encode('utf-8'))
         record['museumtable'] = finallist
         

         scraperwiki.sqlite.save(['museumtable'],record)
