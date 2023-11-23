import scrapy

# Part 1 : Introduction & explications


# Part 2 : Setup virtual env & setup scrapy
# pip install virtualenv (on windows if not venv installed already)
# python3 -m venv venv (create a venv)
# source venv/bin/activate (activate the venv > appears in brackets () in the terminal once done) antyhing we installed will be installed into this folder (only specific to this project)
# pip3 install scrapy (install scrapy in python terminal) ou sudo pip3 install scrapy


#Part 3: Setting up the scrapy project
    # how to create a scrapy project using scrapy
        # terminal : scrapy startproject name_of_the_project (scrapy startproject movies_imdb_scraper)
    # overview of the scrapy project
    # explaining scrapy spiders, items, item pipelines
        # spiders = folder of spiders (fichiers.py avec fonctions etc)
        # item = fichier items.py to define what the items will look like (title, description, etc)
        # item pipeline = fichier.py with function to save the item in the DataBase
    # explaining scrapy middlewares & settings
        # all the middlewares go to the file : middlewares.py 
        # middlewares (how you want the spiders to operate); gives you control over timing out requests, what headers you want to send when you make requests... managing caches, cookies, multiple retries...
            #2 types of middlewares : (1) downloader middlewares =
                                    # (2) spider middlewares = adding or removing requests or items, handling different exceptions that crop up if there's an error for example...
        # settings.py
            # = it's where you put all the settings : do we obey our robots.txt file when initial request is made to a website, the nb of request we maken 10 requests at a time or less or more... 
            # we can enable or disable what we want, we can enable/disable our spider_middlewares, downloader_middleware, item_pipeline for example...
            

