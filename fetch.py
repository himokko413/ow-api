import os
import errno
from beautifulscraper import BeautifulScraper as scr
import datetime

ctime = datetime.datetime.now()
ctime = ctime.strftime("%Y/%j/%H.%M.%S")

web = scr()

from ask import askId

upl = askId();

fn = "data/" + upl + "/" + ctime + ".html"
page = web.go("https://playoverwatch.com/en-us/career/" + upl)
os.makedirs(os.path.dirname(fn), exist_ok=True)
with open(fn, 'w') as f:
	f.write(page.prettify())
