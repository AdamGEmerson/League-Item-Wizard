# League Item Scraper
A small app that scrapes www.champion.gg for the highest win rate item builds and most common item builds. The app formats 
the builds into a JSON file for champion. From there the files can be easily imported into the client.  To learn how to import
item sets check out: https://lol.gamepedia.com/V7.20#Item_Set_Sharing

* Requires BeautifulSoup from the bs4 package, but otherwise it only uses built in packages.  

* To run the app simply navigate to the LeagueItemScraper folder and run `app.py `.  From there a folder will be created with a seperate JSON file for each champion.

* If you want to leave the "Consumables" block off of your item sets you can do so by passing `consumables=False` into the 
`Generate_Json()` function where it is called.

I would love to figure out a way to mass import all the JSON files at once, but it doesn't seem like there is currently a way to do so. You can either import the files for the champions you play or you can import all the files one by one.

The app is not currently set up to update automatically when a new champion comes out but I have plans to add support for that in the future.



