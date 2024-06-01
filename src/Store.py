from Person import Worker, Manager, StoreManager
class Store:
    def __init__(self, store_name: str, worker: list, managers: list, store_manager: str):
        self.store_name = store_name
        self.worker = worker
        self.managers = managers
        self.store_manager = store_manager
        self.stock = ['deb', 'dab']

    def show_people(self):
            worker_list = '\n'.join(self.worker)
            managers_list = '\n'.join(self.managers)
            print(f'''
    In this store are working:
    Workers:
    {worker_list}

    Managers:
    {managers_list}

    Store Manager:
    {self.store_manager}
    ''')
    def show_stock(self):
        print('Currently we have these items in stock:')
        for items in self.stock:
            print(items)


    def load_item_list(self, filename: str):
        with open(filename, 'r') as file:
            for line in file:
                item_details = line.strip().split(',')
                if len(item_details) == 4:
                    name, price, amount, item_code = item_details
                    self.stock.append({
                        'name': name,
                        'price': price,
                        'amount': amount,
                        'item_code': item_code
                    })

    def remove_item_list(self):
        self.stock = []
        with open('product_list.txt', 'w') as file:
            file.truncate()

    def add_worker(self, worker: Worker):
        self.workers.append(worker)

    def add_manager(self, manager: Manager):
        self.managers.append(manager)

    def set_store_manager(self, store_manager: StoreManager):
        self.store_manager = store_manager
