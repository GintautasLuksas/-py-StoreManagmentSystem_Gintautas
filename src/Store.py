class Store:
    def __init__(self, store_name: str, worker: list, managers: list, store_manager: str):
        self.store_name = store_name
        self.worker = worker
        self.managers = managers
        self.store_manager = store_manager
        self.stock = []

    def show_people(self):
        print(f'''
In this store are working:
{self.worker}
{self.managers}
{self.store_manager}.''')
    def show_stock(self):
        print()
        for items in self.stock:
            print('Currently we have these items in stock:')
            print(items)

