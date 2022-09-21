productos = {
    "nombre": [],
    "cantidad": []
}
producto = input("ingrese el producto")
cantidad = int(input("ingrese la cantidad"))

productos["nombre"].append(producto)
productos["cantidad"].append(cantidad)
print(productos)
## para hacer listas dentro de otras listas 