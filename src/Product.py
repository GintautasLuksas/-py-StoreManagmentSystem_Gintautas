class Product:
    def __init__(self, name: str, price: int, amount: int, item_code: int):
        self.name = name
        self.price = price
        self.amount = amount
        self.item_code = item_code

    def edit_name(self, edited: str):
        self.name = edited

    def edit_code(self, new_code: int):
        self.item_code = new_code

    def add_item(self):
        with open('product_list.txt', 'a') as file:
            product_details = f'{self.name},{self.price},{self.amount},{self.item_code}\n'
            file.write(product_details)

    def remove_item(self: int):
        try:
            with open('product_list.txt', 'r') as file:
                lines = file.readlines()

            with open('product_list.txt', 'w') as file:
                for line in lines:
                    if line.strip():
                        details = line.split(',')
                        if str(self) != details[3].strip():
                            file.write(line)
        except FileNotFoundError:
            print("The file 'product_list.txt' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_products(self):
        with open('product_list.txt') as file:
            print(file.read())


class Dry_storage(Product):
    def __init__(self,name: str, price: int, amount: int, item_code: int, is_recipe: bool, is_chemical: bool, package: str ):
        super().__init__(name, price, amount, item_code )
        self.is_recipe = is_recipe
        self.is_chemical = is_chemical
        self.package = package
    def check_recipe(self):
        if self.is_recipe:
            print('This item is part of a recipe.')
        else:
            print('This item is not part of a recipe.')
    def check_chemical(self):
        if self.is_chemical:
            print('This chemical is hazardous.')
        else:
            print('This chemical is not hazardous.')
        return self.is_chemical
    def dry_package_info(self):
        print(f'This product package is: {self.package}.')
class Food(Product):
    def __init__(self, name: str, price: int, amount: int, item_code: int, expiry_date: str, storage_conditions: str):
        super().__init__(name, price, amount, item_code)
        self.expiry_date = expiry_date
        self.storage_condition = storage_conditions

    def check_expiry(self):
        print(f'The expiry date of {self.name} is {self.expiry_date}.')

    def check_storage_conditions(self):
        print(f'The storage conditions for {self.name} are: {self.storage_conditions}.')