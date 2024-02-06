import csv

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.precio}"


class Catalogo:
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = []
        self.cargar_catalogo()

    def cargar_catalogo(self):
        try:
            with open(self.archivo, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    nombre, precio = row
                    self.productos.append(Producto(nombre, float(precio)))
        except FileNotFoundError:
            print("El archivo del catálogo no existe. Se creará uno nuevo al guardar.")

    def guardar_catalogo(self):
        with open(self.archivo, "w", newline="") as file:
            writer = csv.writer(file)
            for producto in self.productos:
                writer.writerow([producto.nombre, producto.precio])

    def alta(self, producto):
        self.productos.append(producto)
        self.guardar_catalogo()

    def baja(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto)
                self.guardar_catalogo()
                return
        print("El producto no está en el catálogo.")

    def consulta(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def modificacion(self, nombre, nuevo_nombre, nuevo_precio):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.nombre = nuevo_nombre
                producto.precio = nuevo_precio
                self.guardar_catalogo()
                print("Producto modificado.")
                return
        print("El producto no está en el catálogo.")

    def lista(self):
        return self.productos

    def __str__(self):
        if not self.productos:
            return "El catálogo está vacío."
        else:
            catalogo_str = ""
            for producto in self.productos:
                catalogo_str += str(producto) + "\n"
            return catalogo_str


def menu():
    print("\n1. Alta de producto")
    print("2. Baja de producto")
    print("3. Consulta de producto")
    print("4. Modificación de producto")
    print("5. Listar productos")
    print("6. Salir")


def main():
    archivo_catalogo = "catalogo.csv"
    catalogo = Catalogo(archivo_catalogo)

    while True:
        menu()
        opcion = input("\nIngrese el número de opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto en euros: "))
            producto = Producto(nombre, precio)
            catalogo.alta(producto)
            print("Producto agregado al catálogo.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a dar de baja: ")
            catalogo.baja(nombre)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a consultar: ")
            producto = catalogo.consulta(nombre)
            if producto:
                print(producto)
            else:
                print("El producto no está en el catálogo.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto en euros: "))
            catalogo.modificacion(nombre, nuevo_nombre, nuevo_precio)

        elif opcion == "5":
            print(catalogo)

        elif opcion == "6":
            print("Guardando cambios y saliendo del programa...")
            catalogo.guardar_catalogo()
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")


if __name__ == "__main__":
    main()
