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

    "General controllers"

    def main_menu(self):
        o = '0'
        while o != '4':
            self.view.main_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.clients_menu()
            elif o == '2':
                self.orders_menu()
            elif o == '3':
                self.products_menu()
            elif o == '4':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    "Controllers for products"
    def products_menu(self):
        o = '0'
        while o != '6':
            self.view.main_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_product()
            elif o == '2':
                self.read_product()
            elif o == '3':
                self.read_all_products()
            elif o == '4':
                self.update_product()
            elif o == '5':
                self.delete_product()
            else:
                self.view.not_valid_option()
        return

    def ask_product(self):
        self.view.ask('Nombre')
        name = input()
        self.view.ask('Marca')
        brand = input()
        self.view.ask('Descripcion')
        descrip = input()
        self.view.ask('Precio')
        price = input()
        return [name, brand, descrip, price]

    def create_product(self):
        name, brand, descrip, price = self.ask_product()
        out = self.model.create_product(name, brand, descrip, price)
        if out == True:
            self.view.ok(name+' '+brand, 'agrego')
        else:
            self.view.error('No se pudo agregar producto')
        return

    def read_product(self):
        self.view.ask('ID producto')
        id_product = input()
        product = self.model.read_product(id_product)
        if type(product) == tuple:
            self.view.show_product(product)
        else:
            if product == None:
                self.view.error('El producto no existe')
            else:
                self.view.error('Error interno')
        return
    def read_all_products(self):
        products = self.model.read_all_products()
        if type(products) == list:
            for product in products:
                self.view.show_product(product)
        else:
            self.view.error('Error interno')
        return
    
    def update_product(self):
        self.view.ask('ID de producto a modificar:')
        product_id = input()
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual)')
        whole_vals = self.ask_product()
        fields, vals = self.update_lists(['name', 'price', 'brand', 'descr'], whole_vals)
        vals.append(product_id)
        vals = tuple(vals)
        out = self.model.update_product(fields, vals)
        if out == True:
            self.view.ok(product_id, 'actualizo')
        else:
            self.view.error('Error interno')
        return

    def delete_product(self):
        self.view.ask('id de producto a borrar:')
        product_id = input()
        count = self.model.delete_product(product_id)
        if count != 0:
            self.view.ok(product_id, 'borro')
        else:
            if count == 0:
                self.view.error('el producto no eixste')
            else:
                self.view.error('error interno')
        return
    
    "Controllers for clients"

    def clients_menu(self):
        o = '0'
        while o != '6':
            self.view.clients_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_client();
            elif o == '2':
                self.read_client();
            elif o == '3':
                self.read_all_clients();
            elif o == '4':
                self.update_client();
            elif o == '5':
                self.delete_client();
            elif o == '6':
                return
            else: 
                self.view.not_valid_option()
        return