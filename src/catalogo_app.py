import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import csv
import pandas as pd

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.precio}"

class CatalogoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi Aplicación de Catálogo")
        self.geometry("800x400")

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.archivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Cargar Catálogo", command=self.cargar_catalogo)
        self.archivo_menu.add_command(label="Guardar Catálogo", command=self.guardar_catalogo)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.salir)

        self.catalogo_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Catálogo", menu=self.catalogo_menu)
        self.catalogo_menu.add_command(label="Listar Catálogo", command=self.listar_catalogo)
        self.catalogo_menu.add_separator()
        self.catalogo_menu.add_command(label="Alta de Producto", command=self.alta_producto)
        self.catalogo_menu.add_command(label="Baja de Producto", command=self.baja_producto)
        self.catalogo_menu.add_command(label="Consulta de Producto", command=self.consultar_producto)
        self.catalogo_menu.add_command(label="Modificación de Producto", command=self.modificar_producto)

        self.productos = []

        self.label = tk.Label(self, text="¡Bienvenido a la aplicación de catálogo!")
        self.label.pack()

        self.button = tk.Button(self, text="Cargar catálogo", command=self.cargar_catalogo)
        self.button.pack()

    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje", "¡Hola! Esto es un mensaje de ejemplo.")

    def cargar_catalogo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivo CSV", "*.csv"), ("Archivo Excel", "*.xlsx")])
        if archivo:
            if archivo.endswith('.csv'):
                self.cargar_csv(archivo)
            elif archivo.endswith('.xlsx'):
                self.cargar_excel(archivo)
            else:
                messagebox.showerror("Error", "Formato de archivo no compatible.")

    def cargar_csv(self, archivo):
        try:
            with open(archivo, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    nombre, precio = row
                    self.productos.append(Producto(nombre, float(precio)))
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo del catálogo no existe. Se creará uno nuevo al guardar.")

    def cargar_excel(self, archivo):
        try:
            df = pd.read_excel(archivo, engine='openpyxl')
            for index, row in df.iterrows():
                nombre, precio = row
                self.productos.append(Producto(nombre, float(precio)))
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo del catálogo no existe. Se creará uno nuevo al guardar.")

    def guardar_catalogo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivo CSV", "*.csv")])
        if archivo:
            with open(archivo, "w", newline="") as file:
                writer = csv.writer(file)
                for producto in self.productos:
                    writer.writerow([producto.nombre, producto.precio])

    def salir(self):
        self.destroy()

    def listar_catalogo(self):
        if self.productos:
            messagebox.showinfo("Catálogo", "\n".join(str(producto) for producto in self.productos))
        else:
            messagebox.showinfo("Catálogo", "El catálogo está vacío.")

    def alta_producto(self):
        nombre = tk.simpledialog.askstring("Alta de Producto", "Ingrese el nombre del producto:")
        if nombre:
            precio = tk.simpledialog.askfloat("Alta de Producto", "Ingrese el precio del producto:")
            if precio:
                self.productos.append(Producto(nombre, precio))
                messagebox.showinfo("Alta de Producto", "Producto agregado al catálogo.")


    def baja_producto(self):
        nombre = simpledialog.askstring("Baja de Producto", "Ingrese el nombre del producto a dar de baja:")
        if nombre:
            for producto in self.productos:
                if producto.nombre == nombre:
                    self.productos.remove(producto)
                    messagebox.showinfo("Baja de Producto", "Producto eliminado del catálogo.")
                    return
            messagebox.showerror("Error", "El producto no está en el catálogo.")

    def consultar_producto(self):
        nombre = simpledialog.askstring("Consulta de Producto", "Ingrese el nombre del producto a consultar:")
        if nombre:
            for producto in self.productos:
                if producto.nombre == nombre:
                    messagebox.showinfo("Consulta de Producto", str(producto))
                    return
            messagebox.showerror("Error", "El producto no está en el catálogo.")

    def modificar_producto(self):
        nombre = simpledialog.askstring("Modificación de Producto", "Ingrese el nombre del producto a modificar:")
        if nombre:
            for producto in self.productos:
                if producto.nombre == nombre:
                    nuevo_nombre = simpledialog.askstring("Modificación de Producto", "Ingrese el nuevo nombre del producto:")
                    if nuevo_nombre:
                        nuevo_precio = simpledialog.askfloat("Modificación de Producto", "Ingrese el nuevo precio del producto:")
                        if nuevo_precio:
                            producto.nombre = nuevo_nombre
                            producto.precio = nuevo_precio
                            messagebox.showinfo("Modificación de Producto", "Producto modificado.")
                            return
            messagebox.showerror("Error", "El producto no está en el catálogo.")

if __name__ == "__main__":
    app = CatalogoApp()
    app.mainloop()
