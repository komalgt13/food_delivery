import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="KomalonmySQL",
    database="food_delivery"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Function to execute an SQL query
def execute_query(query, values=None):
    cursor.execute(query, values)
    connection.commit()

# Function to generate random datetime within a range
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Function to generate mock data for the customer table
def generate_customer_data():
    customer_data = [("Komal", 2.30, 4.50, "komal@desisascendeducare.in", 1), ("Mudit", 7.70, 9.45, "mudit@gmail.com", 2)]
    return customer_data

# Function to insert customer data into the database
def insert_customer_data(data):
    query = "INSERT INTO customer (name, x_coordi, y_coordi, e_mail, user_id) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the additional table
def generate_additional_data():
    fake = Faker()
    additional_data = (1, 1, 1, "pista")
    return additional_data

# Function to insert additional data into the database
def insert_additional_data(data):
    query = "INSERT INTO additional (order_id, category_id, restaurant_id, item_toadd) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the category table
def generate_category_data(num_records):
    fake = Faker()
    category_data = [("Sweets", 1), ("Burgers", 2)]
    return category_data

def generate_category_item_data(num_records):
    fake = Faker()
    category_data = [(1, "Gulabjamun", 250), (2, "mactikki", 220), (1, "barfi", 550)]
    return category_data

# Function to insert category data into the database
def insert_category_data(data):
    query = "INSERT INTO category (name, category_id) VALUES (%s, %s)"
    execute_query(query, data)

# Function to insert category items into the database
def insert_category_item_data(data):
    query = "INSERT INTO category_items (category_id, item_name, calories) VALUES (%s, %s, %s)"
    execute_query(query, data)


# Function to generate mock data for the coupon table
def generate_coupon_data():
    coupon_data = [(1, 1, 10), (2, 2, 50)]
    return coupon_data

# Function to insert coupon data into the database
def insert_coupon_data(data):
    query = "INSERT INTO coupon (coupon_id, user_id, discount) VALUES (%s, %s)"
    execute_query(query, data)

# Function to generate mock data for the delivery table
def generate_delivery_data():
    fake = Faker()
    delivery_data = [("ramesh", 5, 1, "0987654321"), ("suresh", 4, 2, "7890654321")]
    return delivery_data

# Function to insert delivery data into the database
def insert_delivery_data(data):
    query = "INSERT INTO delivery (name, net_rating, delivery_id, phone) VALUES (%s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the ingredients table
def generate_ingredients_data(num_records, category_ids):
    fake = Faker()
    ingredients_data = [(1, "gulabjamun", "milk, pista, khoya, sugar"), (1, "barfi", "milk, cashews, sugar"), (2, "mactikki", "wheat bun, paprika, lettuce, tikki, mustard sauce")]
    return ingredients_data

# Function to insert ingredients data into the database
def insert_ingredients_data(data):
    query = "INSERT INTO ingredients (category_id, item_name, ingredient_name) VALUES (%s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the menu table
def generate_menu_data(num_records, category_ids, restaurant_ids):
    menu_data = ((1, 1), (1, 2), (2, 1))
    return menu_data

# Function to insert menu data into the database
def insert_menu_data(data):
    query = "INSERT INTO menu (restaurant_id, category_id) VALUES (%s, %s)"
    execute_query(query, data)

# Function to generate mock data for the order_ table
def generate_order_data():
    order_data = ("dispatched", 1, 500, 20, "2024:01:21:13:00:00", 1, 1, 1, 1)
    return order_data

# Function to insert order data into the database
def insert_order_data(data):
    query = "INSERT INTO order_ (order_status, user_id, total_price, tip, order_date_time, coupon_code, delivery_id, restaurant_id, order_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the order_item table
def generate_order_item_data():
    fake = Faker()
    order_item_data = [(1, 1, 1, "barfi", 1, "sweets", 200), (1, 1, 2,"mactikki",2, "burger",320)]
    return order_item_data

# Function to insert order_item data into the database
def insert_order_item_data(data):
    query = "INSERT INTO order_item (order_id, restaurant_id, category_id, item_name, quantity, name, cost) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the order_location table
def generate_order_location_data(num_records, order_ids, delivery_ids, user_ids):
    order_location_data = (1, 1, 1, 2.3, 4.5)
    return order_location_data

# Function to insert order_location data into the database
def insert_order_location_data(data):
    query = "INSERT INTO order_location (order_id, delivery_id, user_id, x_coordinate, y_coordinate) VALUES (%s, %s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the payment table
def generate_payment_data():
    payment_data = (1, "wallet", 510, 1, 1)
    return payment_data

# Function to insert payment data into the database
def insert_payment_data(data):
    query = "INSERT INTO payment VALUES (%s, %s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the phone_customer table
def generate_phone_customer_data():
    phone_customer_data = [(1, "0987654321"), (1, "1234567890"), (2, "8219617753")]
    return phone_customer_data

# Function to insert phone_customer data into the database
def insert_phone_customer_data(data):
    query = "INSERT INTO phone_customer (user_id, phone) VALUES (%s, %s)"
    execute_query(query, data)

# Function to generate mock data for the rating table
def generate_rating_data():
    fake = Faker()
    rating_data = [("the food was well cooked and perfect for summers",5, 1, 5,1,1), ("The food was not well cooked", 4, 2, 3, 10, 2)]
    return rating_data

# Function to insert rating data into the database
def insert_rating_data(data):
    query = "INSERT INTO rating (customer_feedback, delivery_rating, delivery_id, order_rating, order_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the restaurant_item_price table
def generate_restaurant_item_price_data():
    restaurant_item_price_data = [(1, 1, 100,"gulabjamun"), (1, 1, 200, "barfi"), (1, 2, 300, "mactikki"), (2, 1, 250, "barfi"), (2, 1, 80, "gulabjamun")]
    return restaurant_item_price_data

# Function to insert restaurant_item_price data into the database
def insert_restaurant_item_price_data(data):
    query = "INSERT INTO restaurant_item_price (restaurant_id, category_id, price_item_restaurant, item_name) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)


# Function to generate mock data for the restaurant table
def generate_restaurant_data(num_records):
    restaurant_data = ("milk bar", 5.50, 6.60, 5, 1, "0987654321")
    return restaurant_data

# Function to insert restaurant data into the database
def insert_restaurant_data(data):
    query = "INSERT INTO restaurant (name, x_coordinate, y_coordinate, net_rating, restaurant_id, contact) VALUES (%s, %s, %s, %s, %s)"
    execute_query(query, data)

# Function to generate mock data for the wallet table
def generate_wallet_data():
    wallet_data = [(1000, 1), (600, 2)]
    return wallet_data

# Function to insert wallet data into the database
def insert_wallet_data(data):
    query = "INSERT INTO wallet (amount, user_id) VALUES (%s, %s)"
    execute_query(query, data)

# Generate and insert mock data for the customer table
def insert_customer_data(data):
    query = "INSERT INTO customer (name, x_coordi, y_coordi, e_mail) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)  

# Generate and insert mock data for the additional table
customer_data = generate_customer_data()
insert_customer_data(customer_data)

# Generate and insert mock data for the restaurant table
restaurant_data = generate_restaurant_data()
insert_restaurant_data(restaurant_data)

# Generate and insert mock data for the category table
record=generate_category_data()
insert_category_data(record)

record=generate_category_item_data()
insert_category_item_data(record)

# Generate and insert mock data for the delivery table
delivery_data = generate_delivery_data()
insert_delivery_data(record)

# Generate and insert mock data for the coupon table
coupon_data = generate_coupon_data()
insert_coupon_data(record)

# Generate and insert mock data for the order_ table
order_data = generate_order_data()
insert_order_data(record)

# Generate and insert mock data for the additional table
additional_data = generate_additional_data()
insert_additional_data(additional_data)

# Generate and insert mock data for the ingredients table
ingredients_data = generate_ingredients_data(15, range(1, 6))
insert_ingredients_data(record)

# Generate and insert mock data for the menu table
menu_data = generate_menu_data()
insert_menu_data(record)

# Generate and insert mock data for the order_item table
order_item_data = generate_order_item_data()
insert_order_item_data(record)

# Generate and insert mock data for the order_location table
order_location_data = generate_order_location_data()
insert_order_location_data(record)

# Generate and insert mock data for the payment table
payment_data = generate_payment_data()
insert_payment_data(record)

# Generate and insert mock data for the phone_customer table
phone_customer_data = generate_phone_customer_data()
insert_phone_customer_data(record)

# Generate and insert mock data for the rating table
rating_data = generate_rating_data()
insert_rating_data(record)

# Generate and insert mock data for the restaurant_item_price table
restaurant_item_price_data = generate_restaurant_item_price_data()
insert_restaurant_item_price_data(record)

# Generate and insert mock data for the wallet table
wallet_data = generate_wallet_data()
insert_wallet_data(record)

# Close the database connection
cursor.close()
connection.close()
