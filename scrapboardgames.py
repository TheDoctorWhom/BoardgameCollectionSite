from lxml import html
from lxml.cssselect import CSSSelector
import requests
import time


seasons = [

"All Creatures big and small",
"all queens chess",
"anatomy park",
"Captain treasure boots",
"Cranium",
"diamonds",
"entropy",
"Firefly out of the black",
"forbidden island",
"galaxy trucker",
"Ghostbuster",
"Gloom",
"how to rob a bank",
"Indiana Jones DVD Adventure game",
"jurassic park danger",
"kill doctor lucky",
"king of tokyo",
"Lanterns",
"lock and key",
"melee",
"morsels",
"munchkin quest",
"munchkins",
"mysterium",
"orphan black",
"outrage",
"Pack and stack",
"pandemic",
"portal the uncooperative cake",
"posthuman",
"race for the galaxy",
"random encounter",
"Scrabble",
"Settlers of Catan card game",
"settlers of Catan",
"slap 45",
"smash up",
"solitaire chess",
"sonar",
"Spacetea",
"Splender",
"Star Trek deck-building game",
"survive escape from Atlantis",
"survive space attack",
"takenoko",
"Teenage Mutant Ninja Turtles Shadows",
"terra mystica",
"the infinite board game",
"the resistanc",
"then they held hands",
"Ticket to Ride New York",
"ticket to ride",
"time stories",
"vinetta",
"where in the world is carmen sandiego",
"zombies!!",]

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
	print("<DIFFICULTY>null</DIFFICULTY>")
	print("<PLAYERS>null</PLAYERS>")
	print("<TIME>null</TIME>")
	print("<TYPE>null</TYPE>")
	print("</GAME>")
