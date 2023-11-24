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
                adapter[lowercase_key] = [item.lower() for item in value_lower]
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


        # int_variables = ['sku', 'length', 'width', 'height']
        # for int_variable in int_variables:
        #     int_value = adapter.get(int_variable)
        #     if isinstance(int_value, str):
        #         # Convertir la chaîne en entier
        #         adapter[int_variable] = int(int_value)
        #     elif isinstance(int_value, list):
        #         # Si la valeur est une liste, convertir chaque élément en entier
        #         adapter[int_variable] = [int(item) for item in int_value]


        # weight_variable = 'weight'
        # weight_value = adapter.get(weight_variable)
        # if isinstance(weight_value, str):
        #     # Nettoyer la chaîne en remplaçant les virgules par des points
        #     weight_value = weight_value.replace(",", '.')
        #     cleaned_value = ''.join(c if c.isdigit() or c == '.' else '' for c in weight_value)
        #     adapter[weight_variable] = float(cleaned_value)
        # elif isinstance(weight_value, list):
        #     cleaned_values = [float(''.join(c if c.isdigit() or c == '.' else '' for c in str(item))) for item in weight_value]
        #     adapter[weight_variable] = cleaned_values[0]
        #     # for decimal_value in cleaned_values[1:]:
        #     #     adapter[weight_variable] += decimal_value / (10 ** len(str(decimal_value)))

    
        # stock_variable = 'stock'
        # stock_value = adapter.get(stock_variable)
        # if isinstance(stock_value, str):
        #     adapter[stock_variable] = int(str(stock_value).strip("[]"))
        # elif isinstance(stock_value, list):
        #     # Convertir la liste en chaîne et retirer les crochets
        #     adapter[stock_variable] = int(str(stock_value).strip("[]"))
        #     for decimal_value in cleaned_values[1:]:
        #         adapter[weight_variable] += decimal_value / (10 ** len(str(decimal_value)))


        # float_variables = ['price']
        # for float_variable in float_variables:
        #     float_value = adapter.get(float_variable)
        #     if isinstance(float_value, str):
        #         adapter[float_variable] = float(float_value.replace(",", '.'))  # Correction ici
        #     elif isinstance(float_value, list):
        #         adapter[float_variable] = [float(item.replace(",", '.')) for item in float_value]


        # list_variables = ['categories', 'tags']
        # for list_variable in list_variables:
        #     list_value = adapter.get(list_variable)
        #     if isinstance(list_value, str):
        #         # Convertir la chaîne en entier
        #         adapter[list_variable] = list_value.lower()
        #     elif isinstance(list_value, list):
        #         # Si la valeur est une liste, convertir chaque élément en entier
        #         adapter[list_variable] = [item.lower() for item in list_value]
        #     else:
        #         adapter[list_variable] = list_value.lower()









        
        
        # for field_name in field_names:
        #     if field_name == 'price':
        #         value = adapter.get(field_name)
        #         adapter[field_name] = float(value)
                
        #     if field_name == 'sku':
        #         sku_value = adapter.get("sku")
        #         adapter[field_name] = int(sku_value)
                
        #     if field_name == 'stock':
        #         stock_string = adapter.get("stock")
        #         # split_string = stock_string.split('')
        #         for character in stock_string:
        #             if character.isdigit() == False:
        #                 stock_string.remove(character)
        #         adapter[field_name] = int(stock_string)
            
        #     if field_name == 'tags':
        #         tags_values = adapter.get("tags")
        #         for tag in tags_values:
        #             tag = tag.title()
        #         adapter[field_name] = tag
            
        return item
