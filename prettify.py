from beautifulscraper import BeautifulScraper

web = BeautifulScraper()

page = web.go("https://playoverwatch.com/en-us/career/pc/himokko413-1907")
file = open("sample-page/pc-prettified.html","w")
file.write(page.prettify().encode('utf-8'));
file.close
