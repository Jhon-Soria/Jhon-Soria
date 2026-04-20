class ProductoAmazonicos :
    def __init__(self, nombre, precio, categoria, stock ):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    #metodo de la clase
    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}. Stock disponible: {self.stock}")

    #avasteser

    def abastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se han abastecido {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")


#aplicar descuento

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        precio_con_descuento = self.precio - descuento
        print(f"El precio de {self.nombre} con un descuento del {porcentaje}% es: {precio_con_descuento:.2f}")


#esta disponible 


    def esta_disponible(self):
        if self.stock > 0:
            print(f"{self.nombre} está disponible. Stock: {self.stock}")
            True
        else:
            print(f"{self.nombre} no está disponible. Stock: {self.stock}")
            False

#crear instancia de la clase productoAmazonicos
producto1 = ProductoAmazonicos("cocona", "futas" , 2.80, 50)
print(producto1.nombre)
print(producto1.precio)
print(producto1.categoria)
print(producto1.stock)

