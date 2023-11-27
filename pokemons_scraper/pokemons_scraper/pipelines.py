# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter

# class SqlitePipeline:
#     def __init__(self) -> None:
#         pass

#         #create/connect to database
#         self.con = sqlite3.connect('pokemons_database.db')

#         #create cursor, used to execute commands
#         self.cur = self.con.cursor()

#         #create tables if none exists
#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS pokemons_data(
#             name TEXT,
#             description TEXT,
#             price FLOAT,
#             sku INTEGER,
#             stock INTEGER,
#             categories TEXT,
#             tags TEXT,
#             weight FLOAT,
#             height INTEGER,
#             width INTEGER,
#             length INTEGER
#             )
#         """)




#     def process_item(self, item, spider):

#         # define insert statement
#         self.cur.execute("""
#                          INSERT INTO pokemons_data (name, description, price, sku, stock, categories, tags, weight, height, width, length) VALUES (?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?)
#                          """,
#                          (
#                             item['name'],
#                             item["description"],
#                             item["price"],
#                             item["sku"],
#                             item["stock"],
#                             item["categories"],
#                             item["tags"],
#                             item["weight"],
#                             item["height"],
#                             item['width'],
#                             item['length']
                            
#                          )
#                          )
        
#         #execute insert of data in database
#         self.con.commit()
        
#         return item


class PokemonsScraperPipeline:


    def __init__(self):

        #create/connect to database
        self.con = sqlite3.connect('pokemons_database.db')

        #create cursor, used to execute commands
        self.cur = self.con.cursor()

        #create tables if none exists
        self.cur.execute("""
                         CREATE TABLE IF NOT EXISTS pokemons_data(
                         
                         categories TEXT,
                         description TEXT,
                         height INTEGER,
                         length INTEGER,
                         name TEXT,
                         price FLOAT,
                         sku INTEGER,
                         stock INTEGER,
                         tags TEXT,
                         weight FLOAT,
                         width INTEGER
                         )

                        """)



    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        #nettoyer le champ stock et le mettre en int
        value_stock = adapter.get('stock')
        value_stock = value_stock.replace(' in stock','') 
        adapter['stock'] = int(value_stock)

        value_poids = adapter.get('weight')
        value_poids = value_poids.replace(' kg','') 
        adapter['weight'] = float(value_poids)

        #mettre en minuscule
        lowercase_keys = ['categories', 'tags']
        for lowercase_key in lowercase_keys:
            value_lower = adapter.get(lowercase_key)

            if isinstance(value_lower, str):
                # Si la valeur est une chaîne, mettre en minuscule
                adapter[lowercase_key] = value_lower.lower()
            elif isinstance(value_lower, list):
                # Si la valeur est une liste, mettre en minuscule chaque élément
                adapter[lowercase_key] = ",".join([item.lower() for item in value_lower])
            else:
                # Gérer d'autres types de données comme vous le souhaitez
                adapter[lowercase_key] = value_lower


        #convertir les string en nombre
        int_keys = ['sku','length', 'width', 'height']
        for int_key in int_keys:
            value = adapter.get(int_key)
            if value is not None:
                adapter[int_key] = int(value)

        #prix converti de string en float
        value_prix = adapter.get('price')
        adapter['price'] = float(value_prix)


        print(type(adapter.get("categories")))


        # define insert statement
        self.cur.execute("""
                         INSERT INTO pokemons_data (categories, description, height, length, name, price, sku, stock, tags, weight, width) VALUES (?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?)
                         """,
                         (

                             adapter.get("categories"),
                             adapter["description"],
                             adapter['height'],
                             adapter['length'],
                             adapter['name'],
                             adapter["price"],
                             adapter["sku"],
                             adapter["stock"],
                             adapter["tags"],
                             adapter["weight"],
                             adapter['width'],
                            
                         )
                         )
        

        # ma_variable = f'''
        # INSERT INTO ma_table (texte, int)
        # VALUES ('{adapter['width']}', {adapter['width']})
        # '''
        # print()
        #execute insert of data in database
        self.con.commit()

            
        return item
