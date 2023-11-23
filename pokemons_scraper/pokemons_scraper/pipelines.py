# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PokemonsScraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        
        for field_name in field_names:
            if field_name == 'price':
                value = adapter.get(field_name)
                adapter[field_name] = float(value)
                
            if field_name == 'sku':
                sku_value = adapter.get("sku")
                adapter[field_name] = int(sku_value)
                
            if field_name == 'stock':
                stock_string = adapter.get("stock")
                # split_string = stock_string.split('')
                for character in stock_string:
                    if character.isdigit() == False:
                        stock_string.remove(character)
                adapter[field_name] = int(stock_string)
            
            if field_name == 'tags':
                tags_values = adapter.get("tags")
                for tag in tags_values:
                    tag = tag.title()
                adapter[field_name] = tag
            
        return item
