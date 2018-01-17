# League Item Scraper
A small app that scrapes www.champion.gg for the highest win rate item builds and most common item builds. The app formats 
the builds into a JSON file for champion. From there the files can be easily imported into the client.  To learn how to import
item sets check out: https://lol.gamepedia.com/V7.20#Item_Set_Sharing

* Requires BeautifulSoup from the bs4 package, but otherwise it only uses built in packages.  

* If you want to leave the "Consumables" block off of your item sets you can do so by passing `consumables=False` into the 
`Generate_Json()` function where it is called.

I would love to figure out a way to mass import the JSON files but it doesn't seem like there is currently a way to do so. You
can just import the files for the champions you play or you can import them all one by one.

