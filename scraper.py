import scraperwiki
import lxml.html
html= scraperwiki.scrape("http://www.alva.org.uk/details.cfm?p=423")
root = lxml.html.fromstring(html)
museumtable=root.cssselect("tbody tr td")
print(museumtable)
