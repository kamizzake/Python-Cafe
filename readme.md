# Python Cafe System ☕

# By Abdul Mueed

## Project Description

This is a my Python Based management system for a Cafe.
It is designed to help two types of users:

1.  **Admins:** To manage the menu inventory and view sales
2.  **Waiters:** To take orders from customers efficiently

I chose this because I had once created a restaurant management system before in C++ that utilized Object Oriented Programming so therefore my choice comes from past experience. My Python cafe management involves real world data relationships (Menu -> Orders -> Stock) which is perfect for demonstrating Object Oriented Programming (OOP) and file handling.

## How To Run

1.  Ensure Pythons Installed
2.  Run Main Program:
    ```bash
    python main.py
    ```
    or however you run py files.
3.  **Admin Password:** `ciao123`

## File Structure

- `main.py`: Entry Point, Handles the main menu and program loop
- `models.py`: Contains `Item` and `Manager` classes. Handles data loading / saving
- `admin.py`: Specific logic for adding items and updating stock
- `waiter.py`: Specific logic for taking orders and searching items
- `utils.py`: Helper functions for visuals (ASCII art, clearing screen) and validation
- `data/`: Folder containing `menu.json` and `orders.json`

## Technical Features

### 1. Object Oriented Programming (OOP)

I used two main classes in `models.py`:

- **Item Class:** Represents a single food item with attributes like `name`, `category`, `price`, and `stock`.
- **Manager Class:** Acts as central controller which manages a list of `Item` objects and a list of order dictionaries. It handles all direct interaction with the JSON files.

### 2. File Persistence

The program automatically creates a `data/` folder.

- **menu.json:** Stores the inventory
- **orders.json:** Stores every completed order

### 3. Regular Expressions (Regex)

I used the `re` module to validate customer phone numbers in `waiter.py`

- **Pattern:** `^\d{11}$`
- **Why:** To ensure that the waiter inputs exactly 11 digits (standard mobile format) before an order is finalized. This prevents bad data from entering the sales records.

### 4. Error Handling

I used `try/except` blocks in multiple places to prevent crashes:

- **Input Validation:** Captures `ValueError` if a user types text instead of numbers for prices or menu selection
- **File Loading:** Checks if JSON files are corrupted or empty before loading to prevent startup crashes

## Design Choices

- **Search By Name:** I decided to allow searching by item name (e.g "Burger") rather than IDs because it is more intuitive for a human waiter
- **Stock Logic:** Stock is decreased _temporarily_ while adding to the cart. If the user cancels the order, the stock is added back. This ensures inventory is always accurate even during the ordering process

## Known Limitations / Future Improvements

- Currently the Admin password is hardcoded. In the future I could store hashed passwords in a file.
- The system is textbased (I run it in VS Code based external console) A future version could use a GUI library like Tkinter.

## Credits

- ASCII Art Based on Designs from [ascii.co.uk](https://ascii.co.uk/art/coffee).
