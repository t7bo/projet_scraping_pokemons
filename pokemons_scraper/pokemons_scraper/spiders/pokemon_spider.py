import scrapy
import re
from pokemons_scraper.items import PokemonItem

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
        # pokemon_item = PokemonItem()
        
        # pokemon_item['name'] = pok.css("h1.product_title::text").get()
        # pokemon_item["price"] = pok.css("p.price .woocommerce-Price-amount::text").get(),
        # pokemon_item["description"] = pok.css("div.woocommerce-product-details__short-description p::text").get(),
        # pokemon_item["stock"] = pok.css("p.stock::text").re(r"(\d+)"), #pok.xpath("//p[@class='stock']/text()").re(r"(\d+) in stock"),
        # pokemon_item["sku"] = pok.css("span.sku::text").get(),
        # pokemon_item["categories"] = pok.css("span.posted_in a::text").getall(),
        # pokemon_item["tags"] = pok.css("span.tagged_as a::text").getall(),
        # pokemon_item["weight"] = pok.xpath("//td[@class='product_weight']/text()").re(r"(\d+)"),
        # # 'dimensions' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)"),
        # pokemon_item['length'] = pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[0],
        # pokemon_item['width'] = pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[1],
        # pokemon_item["height"] = pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[2],
         
        # yield pokemon_item
        
        yield {
                    
        'name' : pok.css("h1.product_title::text").get(),
        "price" : pok.css("p.price .woocommerce-Price-amount::text").get(),
        "description" : pok.css("div.woocommerce-product-details__short-description p::text").get(),
        "stock" : pok.css("p.stock::text").re(r"(\d+)"),
        "sku" : pok.css("span.sku::text").get(),
        "categories" : pok.css("span.posted_in a::text").getall(),
        "tags" : pok.css("span.tagged_as a::text").getall(),
        "weight" : pok.xpath("//td[@class='product_weight']/text()").re(r"(\d+)"),
        # 'dimensions' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)"),
        'length' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[0],
        'width' : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[1],
        "height" : pok.xpath("//td[@class='product_dimensions']/text()").re(r"(\d+) x (\d+) x (\d+)")[2],
         
        }
