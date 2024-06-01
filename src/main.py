import Store
from Person import Worker, Manager, StoreManager
from Product import Product, Dry_storage, Food

# We need to have store to fill it with people and goods.
def create_store():
    store_name = input("Enter store name: ")

    workers = []
    num_workers = int(input("Enter number of workers: "))
    for _ in range(num_workers):
        name = input("Enter worker's name: ")
        phone = int(input("Enter worker's phone number: "))
        email = input("Enter worker's email: ")
        country = input("Enter worker's country: ")
        hourly_rate = float(input("Enter worker's hourly rate: "))
        amount_worked = int(input("Enter worker's amount worked: "))
        workers.append(Worker(name, phone, email, country, hourly_rate, amount_worked))

    managers = []
    num_managers = int(input("Enter number of managers: "))
    for _ in range(num_managers):
        name = input("Enter manager's name: ")
        phone = int(input("Enter manager's phone number: "))
        email = input("Enter manager's email: ")
        country = input("Enter manager's country: ")
        salary = int(input("Enter manager's salary: "))
        responsibility = input("Enter manager's responsibility: ")
        managers.append(Manager(name, phone, email, country, salary, responsibility))

    print("Enter store manager details:")
    name = input("Enter store manager's name: ")
    phone = int(input("Enter store manager's phone number: "))
    email = input("Enter store manager's email: ")
    country = input("Enter store manager's country: ")
    monthly_salary = int(input("Enter store manager's monthly salary: "))
    store_name = input("Enter store manager's store name: ")
    responsibilities = input("Enter store manager's responsibilities (comma separated): ").split(',')
    petty_cash = int(input("Enter store manager's petty cash: "))
    store_manager = StoreManager(name, phone, email, country, monthly_salary, store_name, responsibilities, petty_cash)

    my_store = Store.Store(store_name, workers, managers, store_manager)
    return my_store

#Main menu to control people and products.

def main_menu(my_store):
    print('''
    Welcome to our Store Management system. Please choose your option:
    1. Manage People
    2. Manage Products
    3. Manage Store
    4. Exit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        manage_people_menu(my_store)
    elif choice == '2':
        manage_products_menu(my_store)
    elif choice == '3':
        manage_store_menu(my_store)
    elif choice == '4':
        print("Thanks for using SMS. Bye.")
    else:
        print("Invalid choice. Please enter a valid option.")
        main_menu(my_store)

#Using Person funcionality
def manage_people_menu(my_store):
    print('''
    Manage People Menu:
    1. Add Worker
    2. Add Manager
    3. Add Store Manager
    4. Back to Main Menu
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        add_worker(my_store)
    elif choice == '2':
        add_manager(my_store)
    elif choice == '3':
        add_store_manager(my_store)
    elif choice == '4':
        main_menu(my_store)
    else:
        print("Invalid choice. Please enter a valid option.")
        manage_people_menu(my_store)
def add_worker(my_store):
    name = input("Enter worker's name: ")
    phone = int(input("Enter worker's phone number: "))
    email = input("Enter worker's email: ")
    country = input("Enter worker's country: ")
    hourly_rate = float(input("Enter worker's hourly rate: "))
    amount_worked = int(input("Enter worker's amount worked: "))

    worker = Worker(name, phone, email, country, hourly_rate, amount_worked)
    my_store.workers.append(worker)
    print(f"{name} has been added as a worker to {my_store.store_name}.")
    main_menu(my_store)

def add_manager(my_store):
    name = input("Enter manager's name: ")
    phone = int(input("Enter manager's phone number: "))
    email = input("Enter manager's email: ")
    country = input("Enter manager's country: ")
    salary = int(input("Enter manager's salary: "))
    responsibility = input("Enter manager's responsibility: ")

    manager = Manager(name, phone, email, country, salary, responsibility)
    my_store.managers.append(manager)
    print(f"{name} has been added as a manager to {my_store.store_name}.")
    main_menu(my_store)

def add_store_manager(my_store):
    name = input("Enter store manager's name: ")
    phone = int(input("Enter store manager's phone number: "))
    email = input("Enter store manager's email: ")
    country = input("Enter store manager's country: ")
    monthly_salary = int(input("Enter store manager's monthly salary: "))
    store_name = input("Enter store name: ")
    responsibilities = input("Enter store manager's responsibilities (comma-separated): ").split(',')
    petty_cash = int(input("Enter store manager's petty cash amount: "))

    store_manager = StoreManager(name, phone, email, country, monthly_salary, store_name, responsibilities, petty_cash)
    my_store.store_manager = store_manager
    print(f"{name} has been added as a store manager for {my_store.store_name}.")
    main_menu(my_store)

#Using Product functionality
def manage_products_menu(my_store):
    print('''
    Manage Products Menu:
    1. Add Product
    2. Remove Product
    3. Show Products
    4. Back to Main Menu
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        add_product_to_stock(my_store)
    elif choice == '2':
        remove_product_from_stock(my_store)
    elif choice == '3':
        show_products_in_stock(my_store)
    elif choice == '4':
        main_menu(my_store)
    else:
        print("Invalid choice. Please enter a valid option.")
        manage_products_menu(my_store)

def add_product_to_stock(my_store):
    name = input("Enter product's name: ")
    price = int(input("Enter product's price: "))
    amount = int(input("Enter product's amount: "))
    item_code = int(input("Enter product's item code: "))
    product_type = input("Enter product type (Dry storage/Food): ").lower()

    if product_type == 'dry storage':
        is_recipe = input("Is this item part of a recipe? (True/False): ").lower() == 'true'
        is_chemical = input("Is this item a hazardous chemical? (True/False): ").lower() == 'true'
        package = input("Enter package type: ")
        product = Dry_storage(name, price, amount, item_code, is_recipe, is_chemical, package)
    elif product_type == 'food':
        expiry_date = input("Enter expiry date: ")
        storage_conditions = input("Enter storage conditions: ")
        product = Food(name, price, amount, item_code, expiry_date, storage_conditions)
    else:
        product = Product(name, price, amount, item_code)

    product.add_item()
    print(f"{name} has been added to {my_store.store_name}'s stock.")
    main_menu(my_store)

def remove_product_from_stock(my_store):
    item_code = int(input("Enter item code of the product to remove: "))
    product = Product("", 0, 0, item_code)
    product.remove_item()
    main_menu(my_store)

def show_products_in_stock(my_store):
    print(f"Products in {my_store.store_name}'s stock:")
    with open('product_list.txt') as file:
        print(file.read())
    main_menu(my_store)

#Using Store functionality.
def manage_store_menu(my_store):
    while True:
        print('''
        Manage Store Menu:
        1. Show People
        2. Show Stock
        3. Load Item List
        4. Remove Item List
        5. Back to Main Menu
        ''')
        choice = input("Enter your choice: ")
        if choice == '1':
            my_store.show_people()
        elif choice == '2':
            my_store.show_stock()
        elif choice == '3':
            filename = 'product_list.txt'
            my_store.load_item_list(filename)
            print("Item list loaded successfully.")
            print("Loaded items:")
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
        elif choice == '4':
            my_store.remove_item_list()
            print("Item list removed successfully.")
            main_menu(my_store)
            break
        elif choice == '5':
            main_menu(my_store)
            break
        else:
            print("Invalid choice. Please enter a valid option.")



my_store = create_store()
main_menu(my_store)