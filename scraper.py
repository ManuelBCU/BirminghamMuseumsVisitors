import scraperwiki
import lxml.html
html= scraperwiki.scrape("http://www.alva.org.uk/details.cfm?p=423")

print(html)
