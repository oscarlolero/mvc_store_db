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

    
    def create_zip(self, zip, city, state):
        try:
            sql = 'INSERT into zips(`zip`, `z_city`, `z_state`) values (%s, %s, %s)'
            vals = (zip, city, state)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_zip(self, zip):
        try:
            sql = 'SELECT * FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone() 
            return record
        except connector.Error as err:
            return err
    
    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM zips'
            self.cursor.execute(sql)
            records = self.cursor.fetchall() 
            return records
        except connector.Error as err:
            return err
    
    def read_zips_city(self, city):
        try: 
            sql = 'SELECT * FROM zips Where z_city = %s'
            vals = (city,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
                return err
    
    def update_zips(self, fields, vals):
        try:
            sql = 'UPDATE zips set '+','.join(fields)+'WHERE zip = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_zip(self,zip):
        try:
            sql = 'DELETE from zips where zip = %s' 
            vals = (zip,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    "Product methods"
    def create_product(self, name, brand, descrip, price): 
        try:
            sql = 'INSERT into product (`p_name`, `p_brand`,`p_descrip`,`p_price`) values (%s,%s,%s,%s)'
            vals = (name, brand, descrip, price) 
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_product (self, id_product):
        try:
            sql = 'SELECT * from product where id_product = %s'
            vals = (id_product,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_product_brand(self, brand):
        try:
            sql = 'SELECT * from product where p_brand = %s' 
            vals = (brand,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_products_price_range(self, price_ini, price_end):
        try:
            sql = 'SELECT * from product where p_price >= %s and p_price <= %s'
            vals = (price_ini, price_end)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_all_products(self): 
        try:
            sql = 'SELECT * from product'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_product(self, fields, vals):
        try:
            sql = 'UPDATE product set '+','.join(fields)+'WHERE id_product = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback
            return err
    
    def delete_product(self, id_product):
        try:
            sql = 'DELETE from product where id_product = %s'
            vals = (id_product,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    "client methods"

    def create_client(self, name, sname1, sname2, street, noext, noint, col, zip, email, phone):
        try:
            sql = 'INSERT into clients (`c_fname`, `c_sname1`, `c_sname2`, `c_street`, `c_noext`, `c_noint`, `c_col`, `c_zip`, `c_email`, `c_phone`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (name, sname1, sname2, street, noext, noint, col, zip, email, phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            return err

    def read_a_client(self, id_client):
        try:
            sql = 'SELECT clients.*, zips.z_city, zips.z_state from clients join zips on clients.c_zip = zips.zip and clients.id_client = %s'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_clients_zip(self, zip):
        try:
            sql = 'SELECT clients.*, zips.z_city, zips.z_state from clients join zips on clients.c_zip = zips.zip and clients.c_zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_clients(self): 
        try:
            sql = 'SELECT clients.*, zips.z_city, zips.z_state from clients join zips on clients.c_zip = zips.zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_client(self, fields, vals):
        try:
            sql = 'UPDATE clients set '+','.join(fields)+' WHERE id_client = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_client(self, id_client):
        try:
            sql = 'DELETE from clients where id_client = %s'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    " metodos de ordenes"

    def create_order(self, id_client, status, date, total):
        try:
            sql = 'INSERT into orders (`id_client`,`o_status`,`o_date`,`o_total`) values (%s, %s, %s, %s)'
            vals = (id_client, status, date, total)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            id_order = self.cursor.lastrowid 
            return id_order
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_order(self, id_order):
        try:
            sql = 'SELECT orders.*, clients.*, zips.* from orders join clients on clients.id_client = orders.id_client and orders.id_order = %s join zips on zips.zip = clients.c_zip'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_orders(self): 
        try:
            sql = 'SELECT orders.*, clients.*, zips.* from orders join clients on clients.id_client = orders.id_client join zips on zips.zip = clients.c_zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_orders_date(self, date):
        try:                        
            sql = 'SELECT orders.*, clients.*, zips.* from orders join clients on clients.id_client = orders.id_client and orders.o_date = %s join zips on zips.zip = clients.c_zip'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_orders_clients(self, id_client):
        try:
            sql = 'SELECT orders.*, clients.*, zips.* from orders join clients on  clients.id_client = orders.id_client and orders.id_client = %s join zips on zips.zip = clients.c_zip' #le quite la s a zip
            vals = (id_client,)
            self.cursor.execute (sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_order(self, fields, vals):
        try:
            sql = 'UPDATE orders set '+','.join(fields)+'WHERE id_order = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_order(self, id_order):
        try:
            sql = 'DELETE from orders where id_order = %s'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    "method order details"
    def create_order_detail(self, id_order, id_product, od_amount, od_total):
        try:      
            sql = 'INSERT into order_details (`id_order`,`id_product`,`od_amount`,`od_total`) values (%s, %s, %s, %s)'
            vals = (id_order, id_product, od_amount, od_total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_order_detail(self, id_order, id_product):
        try:
            sql = 'SELECT product.id_product, product.p_name, product.p_brand, product.p_price, order_details.od_amount, order_details.od_total from order_details join product on order_details.id_product = product.id_product and order_details.id_order = %s and order_details.id_product = %s'
            vals = (id_order, id_product)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_order_details(self, id_order):
        try:
            sql = 'SELECT product.id_product, product.p_name, product.p_brand, product.p_price, order_details.od_amount, order_details.od_total from order_details join product on order_details.id_product = product.id_product and order_details.id_order = %s'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_order_details(self, fields, vals):
        try:
            sql = 'UPDATE order_details set '+','.join(fields)+'WHERE id_order = %s and id_product = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_order_details(self,id_order, id_product):
        try:
            sql = 'DELETE from order_details where id_order = %s and id_product = %s'
            vals = (id_order, id_product)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    