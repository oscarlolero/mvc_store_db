from mysql import connector

class Model:
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
    
    def close_db(self):
        self.cnx.close()

    "Products methods"

    def create_product(self, name, brand, description, price):
        try:
            sql = 'INSERT INTO products (`name`, `brand`, `description`, `price`) VALUES(%s, %s, %s, %s)'
            vals = (name, brand, description, price)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    def read_product(self, product_id):
        try:
            sql = 'SELECT * FROM products WHERE product_id = %s'
            vals = (product_id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
            
    def read_all_product(self, product_id):
        try:
            sql = 'SELECT * FROM products'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_products_brand(self, brand):
        try:
            sql = 'SELECT * FROM products WHERE brand = %s'
            vals = (brand, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_all_products_price_range(self, price_ini, price_end):
        try:
            sql = 'SELECT * FROM products WHERE price >= %s AND price <= %s'
            vals = (price_ini, price_end)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_product(self, fields, vals):
        try:
            sql = 'UPDATE products SET'+','.join(fields)+'WHERE product_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_product(self, product_id):
        try:
            sql = 'DELETE FROM products WHERE product_id = %s'
            vals = (product_id, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    "Clients methods"

    def create_client(self, username, password, email, phone, address):
        try:
            sql = 'INSERT INTO clients (`username`, `password`, `email`, `phone`, `address`) VALUES(%s, %s, %s, %s, %s)'
            vals = (username, password, email, phone, address)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_all_clients(self):
        try:
            sql = 'SELECT * FROM clients'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_client(self, fields, vals):
        try:
            sql = 'UPDATE clients SET'+','.join(fields)+'WHERE client_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_client(self, client_id):
        try:
            sql = 'DELETE FROM clients WHERE client_id = %s'
            vals = (client_id, )

            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

        "Order methods"

    def create_order(self, client_id, status, total, date):
        try:
            sql = 'INSERT INTO orders (`client_id`, `status`, `total`, `date`) VALUES(%s, %s, %s, %s)'
            vals = (client_id, status, total, date)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_order(self, order_id):
        try:
            sql = 'SELECT orders.*, clients.* FROM orders JOIN clients ON clients.client_id = orders.client_id AND orders.order_id = %s'
            vals = (order_id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_orders_date(self, date):
        try:
            sql = 'SELECT orders.*, clients.* FROM orders JOIN clients ON clients.client_id = orders.client_id AND clients.date = %s'
            vals = (date,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def read_orders_client(self, client_id):
        try:
            sql = 'SELECT orders.*, clients.* FROM orders JOIN clients ON clients.client_id = orders.client_id AND orders.client_id = %s'
            vals = (client_id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def read_all_orders(self):
        try:
            sql = 'SELECT * FROM orders.*, clients.* JOIN clients clients.order_id = orders.client_id'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_order(self, fields, vals):
        try:
            sql = 'UPDATE orders SET'+','.join(fields)+'WHERE order_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_order(self, order_id):
        try:
            sql = 'DELETE FROM orders WHERE order_id = %s'
            vals = (order_id, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    "Order details methods"

    def create_order_detail(self, order_id, product_id, quantity, total):
        try:
            sql = 'INSERT INTO order_details (`order_id`, `product_id`, `quantity`, `total`) VALUES(%s, %s, %s, %s)'
            vals = (order_id, product_id, quantity, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_order_detail(self, order_id, product_id):
        try:
            sql = 'SELECT products.*, order_detail.total, order_detail.quantity FROM order_details JOIN products ON order_detail.product_id = products.product_id AND order_detail.order_id = %s AND order_detail.product_id = %s'
            vals = (order_id, product_id)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_order_details(self, order_id):
        try:
            sql = 'SELECT products.*, order_detail.total, order_detail.quantity FROM order_details JOIN products ON order_detail.product_id = products.product_id AND order_detail.order_id = %s'
            vals = (order_id,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_order_details(self, fields, vals):
        try:
            sql = 'UPDATE order_details SET'+','.join(fields)+'WHERE order_id = %s AND product_id = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_order_detail(self, order_id, product_id):
        try:
            sql = 'DELETE FROM order_detail WHERE order_id = %s AND product_id = %s'
            vals = (product_id, product_id)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err