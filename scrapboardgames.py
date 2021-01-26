from lxml import html
from lxml.cssselect import CSSSelector
import requests
import time


seasons = [
 		"Boss Monster ",

		"Boss Monste",

		"Bycatch",

		"Chrononaut",

		"Citadel",

		"Dark Storie",

		"Dungeon Buster",

		"Exi",

		"Flux",

		"game",

		"Hanab",

		"Harbou",

		"Himaly",

		"Love Lette",

		"MacGyve",

		"Oregon Trai",

		"Peasant Buffe",

		"Pixel Glor",

		"Sushi G",

		"Total Rickal",

		"Unlock",]

for x in seasons:

	game="https://boardgamegeek.com/geeksearch.php?action=search&objecttype=boardgame&q="+x+"&B1=Go"
	page = requests.get(game)
	tree = html.fromstring(page.content)
	#This will create a list of buyers:
	# title = tree.xpath('//title/text()')
	show = tree.xpath('//*[@id="results_objectname1"]/a/@href')
	# print(show)
	page2 = requests.get("https://boardgamegeek.com"+str(show).lstrip("[']"))
	tree = html.fromstring(page2.content)
	title = tree.xpath('//meta[@name="title"]/@content')
	dis = tree.xpath('//meta[@name="description"]/@content')
	image = tree.xpath('//meta[@property="og:image"]/@content')




	print("<GAME>")
	print("<TITLE>")
	print (str(title).lstrip("[']").rstrip("[']"))
	print("</TITLE>")
	print("<IMAGE>")
	print(str(image).lstrip("[']").rstrip("[']"))
	print("</IMAGE>")
	print("<LINK>")
	print("https://boardgamegeek.com"+str(show).lstrip("[']").rstrip("[']"))
	print("</LINK>")
	print("<DESCRIPTION>")
	print (str(dis).lstrip("[']").rstrip("[']"))
	print("</DESCRIPTION>")
	print("<DIFFICULTY></DIFFICULTY>")
	print("<PLAYERS></PLAYERS>")
	print("<TIME></TIME>")
	print("<TYPE></TYPE>")
	print("</GAME>")
