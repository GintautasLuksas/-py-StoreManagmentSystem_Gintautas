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
                        if int(details[3]) != self:
                            file.write(line)
        except FileNotFoundError:
            print("The file 'product_list.txt' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_products(self):
        with open('product_list.txt') as file:
            print(file.read())
