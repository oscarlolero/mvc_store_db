from model.model import Model
from view.view import View
from datetime import date

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    "controladores generales"
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.zips_menu()
            elif o == '2':
                self.products_menu()
            elif o == '3':
                self.clients_menu()
            elif o == '4':
                self.orders_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return 
    
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs): 
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    "Controladores para zips"
    def zips_menu(self):
        o = '0'
        while o != '7':
            self.view.zips_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_zip()
            elif o == '2':
                self.read_a_zip()
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_zip(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city, state]

    def create_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        city, state = self.ask_zip()
        out = self.model.create_zip(i_zip, city, state)
        if out == True:
            self.view.ok(i_zip, 'agrego')
        else: 
            if out.errno == 1062:
                self.view.error('El CP ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL CP. REVISA.')
        return
    def read_a_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_order_footer()
        else: 
            if zip == None:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ZIP REVISA.')
        return

    def read_all_zips(self):
        zips = self.model.read_all_zips()
        if type(zips) == list:
            self.view.show_zip_header(' Todos los CPs ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else: 
            self.view.error('PROBLEMA AL LEER LOS CPs. REVISA.')
        return

    def read_zips_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_zip_header(' CPs para la ciudad de '+city+' ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else: 
            self.view.error('PROBLEMA AL LEER LOS CPs. REVISA')
        return
    
    def update_zip(self):
        self.view.ask('CP a modificar: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CP. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_zip()
        fields, vals = self.update_lists(['z_city', 'z_state'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zips(fields, vals)
        if out == True:
            self.view.ok(i_zip, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CP. REVISA.')
        return
    
    def delete_zip(self):
        self.view.ask('CP a borrar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count != 0:
            self.view.ok(i_zip, 'borro')
        else:
            if count == 0:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CP. REVISA')
        return
        
    "controladores de productos"
    def products_menu(self):
        o = '0'
        while o != '8':
            self.view.products_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_product()
            elif o == '2':
                self.read_a_product()
            elif o == '3':
                self.read_all_products()
            elif o == '4':
                self.read_products_brand()
            elif o == '5':
                self.read_products_price_range()
            elif o == '6':
                self.update_product()
            elif o == '7':
                self.delete_product()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_product(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Marca: ')
        brand = input()
        self.view.ask('Descripcion: ')
        descrip = input()
        self.view.ask('Precio: ')
        price = input()
        return [name, brand, descrip, price]
    
    def create_product(self):
        name, brand, descrip, price = self.ask_product()
        out = self.model.create_product(name, brand, descrip, price)
        if out == True:
            self.view.ok(name+' '+brand, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL PRODUCTO. REVISA.')
        return
    
    def read_a_product(self):
        self.view.ask('ID producto: ')
        id_product = input()
        product = self.model.read_a_product(id_product)
        if type(product) == tuple:
            self.view.show_product_header(' Datos del producto '+id_product+' ')
            self.view.show_a_product(product)
            self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            if product == None:
                self.view.error('EL PRODUCTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PRODUCTO: REVISA.')
        return
    
    def read_all_products(self):
        products = self.model.read_all_products()
        if type(products) == list:
            self.view.show_product_header(' Todos los productos ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PRODUCTOS. REVISA.')
        return

    def read_products_brand(self):
        self.view.ask('Marca: ')
        brand = input()
        products = self.model.read_product_brand(brand)
        if type(products) == list:
            self.view.show_product_header(' Productos de la marca '+brand+' ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            self.view.error('PROBLEMA LA LEER LOS PRODUCTOS. REVISA.')
        return
    
    def read_products_price_range(self):
        self.view.ask('Precio inferior: ')
        price_ini = input()
        self.view.ask('Precio superior: ')
        price_end = input ()
        products = self.model.read_products_price_range(float(price_ini), float(price_end))
        if type(products) == list:
            self.view.show_product_header(' Productos entre '+price_ini+' y '+price_end+' ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS DATOS. REVISA.')
        return
    
    def update_product(self):
        self.view.ask(' ID de producto a modificar: ')
        id_product = input()
        product = self.model.read_a_product(id_product)
        if type(product) == tuple:
            self.view.show_product_header(' Datos del producto '+id_product+' ')
            self.view.show_a_product(product)
            self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            if product == None:
                self.view.error('EL PRODUCTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PRODUCTO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vaciar para dejar igual):')
        whole_vals = self.ask_product()
        fields, vals = self.update_lists(['p_name','p_brand','p_descrip','p_price'], whole_vals)
        vals.append(id_product)
        vals = tuple(vals)
        out = self.model.update_product(fields, vals)
        if out == True:
            self.view.ok(id_product, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL PRODUCTO. REVISA.')
        return

    def delete_product(self):
        self.view.ask('Id  de producto a borrar: ')
        id_product = input()
        count = self.model.delete_product(id_product)
        if count != 0:
            self.view.ok(id_product, 'borro')
        else:
            if count == 0:
                self.view.error('EL PRODUCTO NO EXISTE')
            else:
                self.view.error('PROBELEMA AL BORRAR EL PRODUCTO. REVISA.')
        return

    
    "controladores del cliente"
    def clients_menu(self):
        o = '0'
        while o != '7':
            self.view.clients_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_client()
            elif o == '2':
                self.read_a_client()
            elif o == '3':
                self.read_all_clients()
            elif o == '4':
                self.read_clients_zip()
            elif o == '5':
                self.update_client()
            elif o == '6':
                self.delete_client()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_client(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno: ')
        sname2 = input()
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('No exterior: ')
        noext = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('CP: ')
        zip = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefono: ')
        phone = input()
        return [name,sname1,sname2,street,noext,noint,col,zip,email,phone]

    def create_client(self):
        name, sname1, sname2, street, noext, noint, col, zip, email, phone = self.ask_client()
        out = self.model.create_client(name, sname1, sname2, street, noext, noint, col, zip, email, phone)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agrego')
        else: 
            self.view.error('NO SE PUDO AGREGAR AL CLIENTE. REVISA.')
        return

    def read_a_client(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header('Datos del cliente '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA.')
        return

    def read_all_clients(self):
        clients = self.model.read_all_clients()
        if type(clients) == list:
            self.view.show_client_header(' Todos los clientes ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS CLIENTES. REVISA.')
        return
    
    def read_clients_zip(self):
        self.view.ask('CP: ')
        zip = input ()
        clients = self.model.read_clients_zip(zip)
        if type(clients) == list:
            self.view.show_client_header(' Clientes en el CP '+zip+' ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS DATOS DEL CLIENTE. REVISA.')
        return

    def update_client(self):
        self.view.ask('ID del cliente a modificar: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header(' Datos del cliente '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_client()
        fields, vals = self.update_lists(['c_fname','c_sname1','c_sname2','c_street','c_noext','c_noint','c_col','c_zip','c_email','c_phone'], whole_vals)
        vals.append(id_client)
        vals = tuple(vals)
        out = self.model.update_client(fields, vals)
        if out == True:
            self.view.ok(id_client, 'actualizo')
        else: 
            self.view.error('NO SE PUDO ACTUALIZAR EL CLIENTE. REVISA.')
        return

    def delete_client(self):
        self.view.ask('ID de cliente a borrar: ')
        id_client = input()
        count = self.model.delete_client(id_client)
        if count != 0:
            self.view.ok(id_client, 'borro')
        else: 
            if count == 0:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CLIENTE. REVISA.')
        return

    "Controladores de la orden"
    def orders_menu(self):
        o = '0'
        while o != '11':
            self.view.orders_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_order()
            elif o == '2':
                self.read_a_order()
            elif o == '3':
                self.read_all_orders()
            elif o == '4':
                self.read_orders_date()
            elif o == '5':
                self.read_orders_client()
            elif o == '6':
                self.update_order()
            elif o == '7':
                self.add_order_details()
            elif o == '8':
                self.update_order_details()
            elif o == '9':
                self.delete_order_details()
            elif o == '10':
                self.delete_order()    
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return

    def create_order(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        o_status = 'processing'
        today = date.today()
        o_date = today.strftime('%y-%m-%d')
        o_total = 0.0
        id_order = self.model.create_order(id_client, o_status, o_date, o_total)
        if type(id_order) == int:
            id_product = ' '
            while id_product != '':
                self.view.msg('---- Agrega productos a la orden (deja vacio el id del producto para salir) ---')
                id_product, od_total = self.create_order_details(id_order)
                o_total += od_total
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        else:
            self.view.error('NO SE PUDO CREAR LA ORDEN. REVISA.')
        return
    
    def read_a_order(self):
        self.view.ask('ID orden: ')
        id_order = input()
        order = self.model.read_a_order(id_order)
        if type(order) == tuple:
            order_details = self.model.read_order_details(id_order)
            if type(order_details) != list and order_details != None:
                self.view.error('PROBLEMA AL LEER LA OREN. REVISA.')
            else:
                self.view.show_order_header(' Datos de la orden '+id_order+' ')
                self.view.show_order(order)
                self.view.show_order_details_header()
                for order_detail in order_details:
                    self.view.show_a_order_details(order_detail)
                self.view.show_order_details_footer()
                self.view.show_order_total(order)
                self.view.show_order_footer()
                return order
        else:
            if order == None:
                self.view.error('LA ORDEN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA ORDEN. REVISA.')
        return
    
    def read_all_orders(self):
        orders = self.model.read_all_orders()
        if type(orders) == list:
            self.view.show_order_header(' Todas la ordenes ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMA AL LEER LA ORDEN '+id_order+'. REVISA.')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS ORDENES. REVISA.')
        return
    
    def read_orders_date(self):
        self.view.ask('Fecha: ')
        date = input()
        orders = self.model.read_orders_date(date)
        if type(orders) == list:
            self.view.show_order_header(' Ordenes para la fecha '+date+' ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMAS LA LEER LA ORDEN '+id_order+'. REVISA.')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS ORDENES. REVISA.')
        return
    
    def read_orders_client(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        orders = self.model.read_orders_clients(id_client)
        if type(orders) == list:
            self.view.show_order_header(' Ordenes para el cliente '+id_client+' ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMAS LA LEER LA ORDEN '+id_order+'. REVISA.')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS ORDENES. REVISA.')
        return
    
    def update_order(self):
        self.view.ask('ID de orden a modificar: ')
        id_order = input()
        order = self.model.read_a_order(id_order)
        if type(order) == tuple:
            self.view.show_order_header(' Datos de la orden '+id_order+' ')
            self.view.show_order(order)
            self.view.show_order_total(order)
            self.view.show_order_footer()
        else:
            if order == None:
                self.view.error('LA ORDEN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA ORDEN. REVISA.')
            return
        self.view.msg('Ingresa los valores a morificar (vacio para dejarlo igual): ')
        self.view.ask('ID Cliente: ')
        id_client = input()
        self.view.ask('Estado (processing, acepted, sent, received): ')
        o_status = input()
        self.view.ask('Fecha (yyyy/mm/dd):')
        o_date = input()
        whole_vals = [id_client, o_status, o_date]
        fields, vals = self.update_lists(['id_client','o_status','o_date'], whole_vals)
        vals.append(id_order)
        vals = tuple(vals)
        out = self.model.update_order(fields, vals)
        if out == True:
            self.view.ok(id_order, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA ORDEN. REVISA.')
        return
    
    def delete_order(self):
        self.view.ask('ID de orden a borrar: ')
        id_order = input()
        count = self.model.delete_order(id_order)
        if count != 0:
            self.view.ok(id_order, 'borro')
        else:
            if count == 0:
                self.view.error('LA ORDEN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA ORDEN. REVISA')
        return
    
    "Controladores para detalles de la orden"
    def create_order_details(self, id_order):
        od_total = 0.0
        self.view.ask('ID producto: ')
        id_product = input()
        if id_product != '':
            product = self.model.read_a_product(id_product)
            if type(product) == tuple:
                self.view.show_product_header(' Datos del producto '+id_product+' ')
                self.view.show_a_product(product)
                self.view.show_product_footer()
                self.view.ask('Cantidad: ')
                od_amount = int(input())
                od_total = od_amount*product[4]
                out = self.model.create_order_detail(id_order, id_product, od_amount, od_total)
                if out == True:
                    self.view.ok(product[1]+' '+product[2], 'agrego a la orden')
                else:
                    if out.errno == 1062:
                        self.view.error('EL PRODUCTO YA ESTA EN LA ORDEN')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL PRODUCTO. REVISA.')
                    od_total = 0.0
            else:
                if product == None:
                    self.view.error('EL PRODUCTO NO EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER EL PRODUCTO. REVISA.')
        return id_product, od_total

    def add_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('---- Agrega productos a la orden (deja vacio el id del producto para salir) ---')
                id_product, od_total = self.create_order_details(id_order)
                o_total += od_total
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        return

    def update_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('---- Modifica productos de la orden (deja vacio el id del producto para salir) ----')
                self.view.ask('ID producto: ')
                id_product = input()
                if id_product != '':
                    order_detail = self.model.read_a_order_detail(id_order, id_product)
                    if type(order_detail) == tuple:
                        od_total_old = order_detail[5]
                        o_total -= od_total_old
                        product = self.model.read_a_product(id_product)
                        price = product[4]
                        self.view.ask('Cantidad: ')
                        od_amount = int(input())
                        od_total = price*od_amount
                        o_total += od_total
                        fields, whole_vals = self.update_lists(('od_amount','od_total'),(od_amount,od_total))
                        whole_vals.append(id_order)
                        whole_vals.append(id_product)
                        self.model.update_order_details(fields, whole_vals)
                        self.view.ok(id_product, 'actualizo en la orden')
                    else:
                        if order_detail == None:
                            self.view.error('EL PRODUCTO NO EXISTE EN LA ORDEN')
                        else:
                            self.view.error('PROBLEMA AL ACTUALIZAR EL PRODUCTO. REVISA.')
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        return
            
    def delete_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('---- Bora productos de la orden (deja vacio el id del producto para salir) ----')
                self.view.ask('ID producto: ')
                id_product = input()
                if id_product != '':
                    order_detail = self.model.read_a_order_detail(id_order, id_product)
                    count = self.model.delete_order_details(id_order, id_product)
                    if type(order_detail) == tuple and count != 0:
                        od_total = order_detail[5]
                        o_total -= od_total
                        self.view.ok(id_product, 'borro de la orden')
                    else:
                        if order_detail == None:
                            self.view.error('EL PRODUCTO NO EXISTE EN LA ORDEN')
                        else: 
                            self.view.error('PROBLEMA AL BORRAR EL PRODUCTO. REVISA.')
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        return
