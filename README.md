# Store Management System (SMS)

The Store Management System (SMS) is a Python-based program designed to facilitate efficient management of a retail store. It provides functionalities for managing personnel, tracking inventory, and overseeing store operations.

## Features

- **Personnel Management:**
  - Add and manage workers, managers, and a store manager.
  - View contact information, salary details, responsibilities, and work-related information.

- **Inventory Management:**
  - Add, remove, and display products in stock.
  - Categorize products into general products, dry storage items, and food items with specific attributes like expiry date, storage conditions, and package type.

- **Store Operations:**
  - Load and remove item lists from inventory files.
  - Manage petty cash, add or remove tasks for the store manager.

## Classes

### Person
Represents basic information about a person such as name, phone number, email, and country.

### Worker
Represents an employee in the store, inheriting from `Person`. Includes hourly rate and amount worked.

### Manager
Represents a manager in the store, inheriting from `Person`. Includes salary and responsibilities.

### StoreManager
Represents the store manager overseeing store operations, inheriting from `Person`. Manages monthly salary, store-specific responsibilities, and petty cash.

### Product
Represents a generic product with attributes like name, price, amount, and item code.

### Dry_storage
Specialized product category inheriting from `Product`, including attributes like whether it's part of a recipe, if it's a hazardous chemical, and package type.

### Food
Specialized product category inheriting from `Product`, including attributes like expiry date and storage conditions.

### Store
Central class managing the store itself, including personnel and inventory operations.
