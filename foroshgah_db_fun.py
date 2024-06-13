import sqlite3
class tables():
    def create_tables():
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            wallet REAL DEFAULT 0
        )
        ''')
        
        # جدول مدیر
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS manager (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')
        
        # جدول محصولات
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT NOT NULL,
            topic TEXT NOT NULL
        )
        ''')
        
        # جدول سفارشات
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customer(id),
            FOREIGN KEY (item_id) REFERENCES items(id)
        )
        ''')
        
        # جدول سبد خرید
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sabad_kharid (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customer(id),
            FOREIGN KEY (item_id) REFERENCES items(id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
class main():
    @staticmethod
    def add_customer(name , last_name , phone_number, username , password):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO customer (name , last_name , phone_number, username , password)
        VALUES (?, ?, ?, ?, ?)
        ''', (name , last_name , phone_number, username , password)
        )
        conn.commit()
        conn.close()
        return f"customer added sucssefuly , your pass word is {password}"
        
    @staticmethod
    def check_customer(username, password):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer WHERE username = ? AND password = ?", (username, password))
        cheak = cursor.fetchone()
        conn.close()
        if cheak:
            return True
        else:
            return False


        
    @staticmethod
    def check_manager(username, password):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM manager WHERE username = ? AND password = ?", (username, password))
        cheak = cursor.fetchone()
        conn.close()
        if cheak:
            return True
        else:
            return False


    @staticmethod
    def add_to_cart(customer_id, item_id, quantity):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO sabad_kharid (customer_id, item_id, quantity)
        VALUES (?, ?, ?)
        ''', (customer_id, item_id, quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def view_cart(customer_id):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT items.name, items.price, sabad_kharid.quantity
        FROM sabad_kharid
        JOIN items ON sabad_kharid.item_id = items.id
        WHERE sabad_kharid.customer_id = ?
        ''', (customer_id,))
        cart_items = cursor.fetchall()
        conn.close()
        return cart_items

    @staticmethod
    def place_order(customer_id):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        # دریافت آیتم های سبد خرید مشتری
        cursor.execute('''
        SELECT item_id, quantity FROM sabad_kharid WHERE customer_id = ?
        ''', (customer_id,))
        cart_items = cursor.fetchall()
        
        # اضافه کردن آیتم ها به جدول سفارشات
        for item in cart_items:
            cursor.execute('''
            INSERT INTO orders (customer_id, item_id, order_date, status)
            VALUES (?, ?, DATE('now'), 'Pending')
            ''', (customer_id, item[0]))
        
        # خالی کردن سبد خرید مشتری
        cursor.execute('''
        DELETE FROM sabad_kharid WHERE customer_id = ?
        ''', (customer_id,))
        
        conn.commit()
        conn.close()


class items():
    def __init__(self, id, name, price, description, topic) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.topic = topic
        
    def add_item(name, price, description, topic):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO items (name, price, description, topic)
        VALUES (?, ?, ?, ?)
        ''', (name, price, description, topic))
        conn.commit()
        conn.close()
    def delete_item(id, name):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()

        cursor.execute('''
        DELETE FROM items WHERE id = ? AND name = ?
        ''', (id, name))
        conn.commit()
        conn.close()
        return True
    def update(id , topic, new_data):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        query = f"UPDATE items SET {topic} = ? WHERE id = ?"
        cursor.execute(query, (new_data, id))
        if cursor.rowcount == 0:
            print("No item found with the given ID.")
            conn.close()
            return False
        conn.commit()
        conn.close()
        return True
        

    def show_all_items():
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        items = cursor.fetchall()
        conn.close()
        return items
    @staticmethod
    def filter(topic):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM items WHERE topic = ?
        ''', (topic,))
        items = cursor.fetchall()
        conn.close()
        if items:
            return items
        else:
            print("No items found in this topic.")
            return []
        