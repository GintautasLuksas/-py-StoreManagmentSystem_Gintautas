import Store
from Person import Worker, Manager, StoreManager
from Product import Product, Dry_storage, Food

# We need to have store to fill it with people and goods.
def create_store():
    store_name = input("Enter store name: ")
    workers = []
    managers = []
    store_manager = StoreManager('Gintautas', 865899658, 'gintautas.luksas@gmail.com', 'Lietuva', 1200, 'Mega', ['Time managment', 'Communication', 'Counting'],  300)

    my_store = Store.Store(store_name, workers, managers, store_manager)
    return my_store

#Main menu to control people and products.

def main_menu(my_store):
    print('''
    Welcome to our Store Management system. Please choose your option:
    1. Manage People
    2. Manage Products
    3. Manage Store
    4. Manage People Info
    5. Exit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        manage_people_menu(my_store)
    elif choice == '2':
        manage_products_menu(my_store)
    elif choice == '3':
        manage_store_menu(my_store)
    elif choice == '4':
        manage_people_info_menu(my_store)
    elif choice == '5':
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
    print("Enter product details:")
    name = input("Enter product's name: ")
    price = float(input("Enter product's price: "))
    amount = int(input("Enter product's amount: "))
    item_code = int(input("Enter product's item code: "))
    product_type = input("Enter product type (Dry Storage or Food): ").lower()

    if product_type == 'product':
        product = Product(name, price, amount, item_code)
    elif product_type == 'dry storage':
        is_recipe = input("Is this item part of a recipe? (True/False): ").lower() == 'true'
        is_chemical = input("Is this item a hazardous chemical? (True/False): ").lower() == 'true'
        package = input("Enter package type: ")
        product = Dry_storage(name, price, amount, item_code, is_recipe, is_chemical, package)
    elif product_type == 'food':
        expiry_date = input("Enter expiry date: ")
        storage_conditions = input("Enter storage conditions: ")
        product = Food(name, price, amount, item_code, expiry_date, storage_conditions)
    else:
        print("Invalid product type.")
        return

    my_store.stock.append(product)
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
        5. _secret Menu
        6. Back to Main Menu
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
            authenticate_and_show_secret_menu(my_store)
        elif choice == '6':
            main_menu(my_store)
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#Secret menu.
def _secret_menu(my_store):
    while True:
        print('''
        Secret Menu:
        1. Manage Petty Cash
        2. Add / Remove Tasks
        3. Back to Main Menu
        ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_petty_cash(my_store)
        elif choice == '2':
            add_remove_tasks(my_store)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def manage_petty_cash(my_store):
    while True:
        print('''
        Manage Petty Cash:
        1. Add to Petty Cash
        2. Remove from Petty Cash
        3. View Current Petty Cash Balance
        4. Back to Secret Menu
        ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to add: "))
            my_store.store_manager._petty_expense(-amount)
            print(f"Added {amount} to petty cash. New balance: {my_store.store_manager.petty_cash}")
        elif choice == '2':
            amount = float(input("Enter amount to remove: "))
            my_store.store_manager._petty_expense(amount)
            print(f"Removed {amount} from petty cash. New balance: {my_store.store_manager.petty_cash}")
        elif choice == '3':
            my_store.store_manager._MGRcash()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def add_remove_tasks(my_store):
    while True:
        print('''
        Add / Remove Tasks:
        1. Add Task
        2. Remove Task
        3. View Tasks
        4. Back to Secret Menu
        ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            my_store.store_manager.add_task(task)
            print(f"Added task: {task}")
        elif choice == '2':
            task = input("Enter task to remove: ")
            if task in my_store.store_manager.responsibilities:
                my_store.store_manager.responsibilities.remove(task)
                print(f"Removed task: {task}")
            else:
                print(f"Task '{task}' not found.")
        elif choice == '3':
            print(f"Current tasks: {', '.join(my_store.store_manager.responsibilities)}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
def authenticate_and_show_secret_menu(my_store):
    password = input("Enter the password to access the secret menu: ")
    if password == "123456":
        _secret_menu(my_store)
    else:
        print("Incorrect password. Access denied.")
        main_menu(my_store)

def manage_people_info_menu(my_store):
    while True:
        print('''
        People info:
        1. Worker information
        2. Manager information
        3. Back to Main Menu
        ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            worker_information(my_store)
        elif choice == '2':
            manager_information(my_store)
        elif choice == '3':

            break
        else:
            print("Invalid choice. Please enter a valid option.")
def worker_information(my_store):
    while True:
        print('''
           Worker information:
           1. Display Amount Worked
           2. Display Rate
           3. Display Salary
           4. Back to Main Menu
           ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            for worker in my_store.workers:
                worker.display_amount_worked()
        elif choice == '2':
            for worker in my_store.workers:
                worker.display_rate()
        elif choice == '3':
            for worker in my_store.workers:
                worker.display_salary()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
def manager_information(my_store):
    while True:
        print('''
           Manager information:
           1. Display Salary
           2. Manager Info
           3. Back to Main Menu
           ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            for manager in my_store.managers:
                manager.display_salary()
        elif choice == '2':
            for manager in my_store.managers:
                manager.mgr_info()
        elif choice == '3':
            main_menu(my_store)
            break
        else:
            print("Invalid choice. Please enter a valid option.")


my_store = create_store()
main_menu(my_store)