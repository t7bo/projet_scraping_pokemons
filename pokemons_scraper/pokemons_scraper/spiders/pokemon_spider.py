import scrapy


class PokemonSpiderSpider(scrapy.Spider):
    name = "pokemon_spider"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    def parse(self, response):
        pokemons_links = response.css("a.woocommerce-LoopProduct-link")
        
        # for pokemon in pokemons_links:
        #     yield {
                
        #     }

        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
