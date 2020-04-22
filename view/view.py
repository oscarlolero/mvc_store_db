class View:
    def start(self):
        print('==========================')
        print('Bienvenido a la tienda.')
        print('==========================')
    
    def end(self):
        print('==========================')
        print('Hasta la vista')
        print('==========================')

    def main_menu(self):
        print('==========================')
        print('Menu principal')
        print('==========================')
        print('1. Clientes')
        print('2. Ordenes')
        print('3. Productos')
        print('4. Salir')
    
    def option(self, last):
        print('Selecciona una opcion (1-)'+last+'):', end = '')

    def not_valid_option(self):
        print('Opcion no valida', end = '')
    
    def ask(self, output):
        print(output)

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('============================')
        print('+ '+id+ 'se' + op + 'correctamente.')
        print('============================')
    
    def error(self, err):
        print('============================')
        print('ERROR: '+ err)
        print('============================')

    "Products views"

    def products_menu(self):
        print('============================\nSubmenu productos\n============================')
        print('1. Agregar producto')
        print('2. Leer producto')
        print('3. Leer todos los productos')
        print('4. Actualizar producto')
        print('5. Borrar producto')
        print('6. Regresar')

    def show_product(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Marca: ', record[2])
        print('Descripcion: ', record[3])
        print('Precio: ', record[4])
        print('============================')

    "Clients views"

    def clients_menu(self):
        print('============================\nSubmenu clientes\n============================')
        print('1. Agregar cliente')
        print('2. Leer cliente')
        print('3. Leer todos los cliente')
        print('4. Actualizar cliente')
        print('5. Borrar cliente')
        print('6. Regresar')

    def show_client(self, record):
        print('ID: ', record[0])
        print('Usuario: ', record[1])
        print('Email: ', record[3])
        print('Telefono: ', record[4])
        print('Direccion: ', record[5])
        print('============================')

    "Orders views"

    def orders_menu(self):
        print('============================\nSubmenu ordenes\n============================')
        print('1. Agregar orden')
        print('2. Leer orden')
        print('3. Leer todas las ordenes')
        print('4. Leer todas las ordenes fecha')
        print('5. Leer todas las ordenes cliente')
        print('6. Actualizar datos orden')
        print('7. Agregar producto a orden')
        print('8. Modificar productos de una orden')
        print('9. Borrar productos de una orden')
        print('10. Borrar orden')
        print('11. Rgresar')

    def show_order(self, record):
        print('ID: ', record[0])
        print('Estado: ', record[3])
        print('Fecha: ', record[4])
        print('Total: ', record[2])
        print('Datos cliente: ')
        self.show_client(record[5:])
        print('============================')

    "View order details"

    def show_order_details(self, record):
        print(record[0]+'\t'+record[1]+'\t'+record[2]+'\t'+record[3]+'\t')
    def show_order_details_header(self):
        print('ID\tProducto\tMarca')