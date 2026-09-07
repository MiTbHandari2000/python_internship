class Shop:

    def __init__(self):
        self.product_list = []
        
    def add_product(self,product_name):

        self.product_list.extend(product_name)
        
        
    def list_product(self):
        
        for item in self.product_list:
            print(item)

fruitlist = Shop()
fruitlist.add_product(["Melons","berries","nuts"])
fruitlist.list_product()