import scrapy
import re


class PokemonSpiderSpider(scrapy.Spider):
    name = "pokemon_spider"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    def parse(self, response):
        pokemons_links = response.css("a.woocommerce-LoopProduct-link")
        
        for pokemon in pokemons_links:
            pokemon_url = pokemon.css("a.woocommerce-LoopProduct-link::attr(href)").get()
            yield response.follow(pokemon_url, callback=self.parse_pokemon_page)
    

        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    
    def parse_pokemon_page(self, response):
        
        pok = response.css("div.content-area")
        
        yield {
            
            'pokemon_name' : pok.css("h1.product_title::text").get(),
            'pokemon_price' : pok.css("p.price .woocommerce-Price-amount::text").get(),
            'pokemon_description' : pok.css("div.woocommerce-product-details__short-description p::text").get(),
            'pokemon_stock' : pok.css("p.stock::text").get(),
            'pokemon_sku' : pok.css("span.sku::text").get(),
            'pokemon_categories' : pok.css("span.posted_in a::text").getall(),
            'pokemon_tags' : pok.css("span.tagged_as a::text").getall(),
            'pokemon_weight' : pok.css(".product_weight::text").get(),
            # 'pokemon_dimensions' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)"),
            'pokemon_length' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[0],
            'pokemon_width' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[1],
            'pokemon_height' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[2],
        
        
        }
         
