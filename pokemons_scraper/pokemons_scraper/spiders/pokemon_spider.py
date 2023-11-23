import scrapy


class PokemonSpiderSpider(scrapy.Spider):
    name = "pokemon_spider"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    def parse(self, response):
        pokemons_links = response.css("a.woocommerce-LoopProduct-link")
        
        
        pokemon_name = response.css("h1.product_title::text").get()
        pokemon_price = response.css("p.price .woocommerce-Price-amount::text").get()
        pokemon_description = response.css("div.woocommerce-product-details__short-description p::text").get()
        pokemon_stock = response.css("p.stock::text").get()
        pokemon_sku = response.css("span.sku::text").get()
        pokemon_categories = response.css("span.posted_in a::text").getall()
        pokemon_tags = response.css("span.tagged_as a::text").getall()
        pokemon_weight = response.css(".product_weight::text").get()
        pokemon_length = 
        pokemon_width = 
        pokemon_height = 
        
        
        
        for pokemon in pokemons_links:
            relative_url = response.css("a.woocommerce-LoopProduct-link").get()
            if relative_url is not None:
                yield response.follow(relative_url, callback=self.parse_pokemon_page)
    

        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    
    def parse_pokemon_page(self, response):
        pass
         
