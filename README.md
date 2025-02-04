# E-Commerce Website (WeStore)

This is a simple e-commerce website built using **Django**, providing essential features like user authentication, product browsing, cart management, and order placement.

## Features

- **User Authentication**
  - Users can sign up, log in, and log out.
  - Password security with validation.
  
- **Product Management**
  - Products are organized by categories.
  - Users can view a list of products, filter by categories, and see details like price and description.
  
- **Shopping Cart**
  - Users can add products to their cart.
  - Cart items can be updated (increase or decrease quantity).
  - Users can remove items from the cart.
  - Total price is dynamically updated based on the cart contents.
  
- **Order Placement**
  - After reviewing the cart, users can place an order.
  - Simple checkout flow for order confirmation.

## Tech Stack

- **Backend**: Django (Python framework)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (by default with Django, easily replaceable with other databases like PostgreSQL, MySQL)
- **Filters**: Custom Django template filters for price calculations

## Installation

1. **Clone this repository**:
  ```bash
  git clone https://github.com/kiranS-2506/WeStore.git
  cd WeStore
  ```
2. **Set up your virtual environment**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate
  ```
3. **Install the required dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

4. **Set up the database:**
    ```bash
    python manage.py migrate
5. **Create a superuser to access the Django admin panel**:
    ```bash
    python manage.py createsuperuser
6. **Run the development server:**
     ```bash
      python manage.py runserver
     ```
## Usage
 - You can visit the home page and browse through the available products.
 - Sign up for an account, log in, and start adding products to your cart.
 - The cart allows you to update the quantities, remove items, and view the total price.
 - After reviewing the cart, you can place an order.

## Contributing
- Contributions are welcome! Please open an issue or submit a pull request.

  
  
## License
  - This project is licensed under the MIT License - see the LICENSE file for details.  

  


  
