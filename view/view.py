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
        print('1. CPs')
        print('2. Productos')
        print('3. Clientes')
        print('4. Ordenes')
        print('5. Salir')
    
    def option(self, last):
        print('Selecciona una opcion (1-'+last+'):', end = '')

    def not_valid_option(self):
        print('Opcion no valida', end = '')
    
    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id)+len(op)+24)))
        print('+ ¡'+str(id)+' se '+op+' Correctamente! +')       
        print('+'*(len(str(id)+len(op)+24)))
    
    def error(self, err):
        print('============================')
        print('¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    "Zips views"

    def zips_menu(self):
        print('============================\nSubmenu CPs\n============================')
        print('1. Agregar CP')
        print('2. Mostrar CP')
        print('3. Mostrar todos los CPs')
        print('4. Mostrar CPs de uan ciudad')
        print('5. Actualizar CP')
        print('7 Borrar Cp')
        print('6. Regresar')
    
    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')

    def show_zip_header(self, header):
        print(header.center(78,'+'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)
    
    def show_zip_midder(self):
        print('-'*78)

    def show_zip_footer(self):
        print('-'*78)

    
    "Products View"
    
    def products_menu(self):
        print('============================\nSubmenu Productos\n============================')
        print('1. Agregar producto')
        print('2. Leer producto')
        print('3. Leer todos los productos')
        print('4. Leer productos de una marca')
        print('5. Leer productos de un rango de precio')
        print('6. Actualizar producto')
        print('7. Borrar producto')
        print('8. Regresar')

    def show_a_product(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Marca:', record[2])
        print('Descripcion:', record[3])
        print('Precio:', record[4])

    def show_product_header(self, header):
        print('-'*48)

    def show_product_midder(self):
        print('-'*48)  

    def show_product_footer(self):
        print('-'*48)     


    "Clients views"

    def clients_menu(self):
        print('============================\nSubmenu clientes\n============================')
        print('1. Agregar cliente')
        print('2. Leer cliente')
        print('3. Leer todos los cliente')
        print('4. Leer clientes de un SP')
        print('5. Actualizar cliente')
        print('6. Borrar cliente')
        print('7. Regresar')

    def show_a_client(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1]+' '+record[2]+' '+record[3])
        print('Direccion: ', record[4]+' '+record[5])+' '+record[6]+' '+record[7]
        print(record[11]+' '+record[12]+' '+record[8])
        print('Email: ', record[9])
        print('Telefono:', record[10])
        print('============================')

    def show_client_header(self, header):
        print(header.center(53,'+'))
        print('+'*53)

    def show_client_midder(self):
         print('+'*53)

    def show_client_footer(self):
         print('+'*53)

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
        print('Estado: ', record[2])
        print('Fecha: ', record[3])
        print('Datos del cliente'.center(81,'*'))
        "self.show_a_client_brief(record[5:])"


    def show_order_header(self, header):
        print(header.center(81,'+'))

    def show_order_midder(self):
        print('+'*81)
    
    def show_order_total(self, record):
        print('Total de la orden'+str(record[4]))
    
    def show_order_footer(self):
        print('+'*81)

    "View order details"

    def show_a_order_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<1}|{record[4]:<9}|{record[5]:<11}')
    
    def show_order_details_header(self):
        print('+'*81)
        print('ID'.ljust(5)+'|'+'Producto'.ljust(20)+'|'+'Marca'.ljust(20)+'|'+'Precio'.ljust(11)+'|'+'Cantidad'.ljust(9)+'|'+'Total'.ljust(11))
        print('+'*81)
    
    def show_order_detail_footer(self):
        print('+'*81)