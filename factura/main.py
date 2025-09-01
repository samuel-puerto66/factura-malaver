import os

INVENTARIO_FILE = "inventario.txt"
FACTURAS_FILE = "facturas.txt"
IVA = 0.19





def leer_archivo(file, parse_func):#funcion para que sirvan las variables
    if not os.path.exists(file): return []
    with open(file, "r") as f:
        return [parse_func(l.strip()) for l in f.readlines()]

def escribir_archivo(file, lista, to_str):
    with open(file, "w") as f:
        f.writelines([to_str(i) + "\n" for i in lista])








def cargar_inventario():
    return leer_archivo(INVENTARIO_FILE, 
        lambda l: {"id": l.split(",")[0], "nombre": l.split(",")[1], 
                   "precio": float(l.split(",")[2]), "cantidad": int(l.split(",")[3])})

def guardar_inventario(inv):
    escribir_archivo(INVENTARIO_FILE, inv, 
        lambda p: f"{p['id']},{p['nombre']},{p['precio']},{p['cantidad']}")

def añadir_producto():
    inv = cargar_inventario()
    inv.append({"id": input("ID: "), "nombre": input("Nombre: "), 
                "precio": float(input("Precio: ")), "cantidad": int(input("Cantidad: "))})
    guardar_inventario(inv)
    print("Producto añadido")

def listar_productos():
    for p in cargar_inventario():
        print(f"ID:{p['id']} | {p['nombre']} | ${p['precio']} | Cantidad:{p['cantidad']}")

def buscar_producto():
    crit = input("Buscar por ID y nombre ").lower()
    inv = cargar_inventario()
    encontrado = next((p for p in inv if p["id"].lower()==crit or p["nombre"].lower()==crit), None)
    print("Encontrado:", encontrado) if encontrado else print("No existe")


def eliminar_producto():
    idp = input("ID a eliminar: ")
    inv = [p for p in cargar_inventario() if p["id"] != idp]
    guardar_inventario(inv); print("🗑 Producto eliminado")








def cargar_facturas(): return leer_archivo(FACTURAS_FILE, eval)#facturas
def guardar_facturas(f): escribir_archivo(FACTURAS_FILE, f, str)

def crear_factura():
    facturas, inv, items, subtotal = cargar_facturas(), cargar_inventario(), [], 0
    fid = len(facturas)+1
    while True:
        listar_productos()
        idp = input("ID producto (salir): ")
        if idp.lower()=="salir": break
        prod = next((p for p in inv if p["id"]==idp), None)
        if prod:
            cant = int(input("Cantidad: "))
            if cant>prod["cantidad"]: print(" Insuficiencia")
            else:
                total_item = prod["precio"]*cant
                items.append({"id":prod["id"],"nombre":prod["nombre"],"cantidad":cant,"total":total_item})
                subtotal+=total_item; prod["cantidad"]-=cant
    if items:
        iva, total = subtotal*IVA, subtotal*(1+IVA)
        factura = {"id":fid,"items":items,"subtotal":subtotal,"iva":iva,"total":total}
        facturas.append(factura); guardar_facturas(facturas); guardar_inventario(inv)
        print("creada")

def listar_facturas():
    for f in cargar_facturas():
        print(f"Factura {f['id']} | Total: ${f['total']}")

def mostrar_factura():
    fid = int(input("ID factura: "))
    f = next((x for x in cargar_facturas() if x["id"]==fid), None)
    if f:
        print(f"\n--- FACTURA {f['id']} ---")
        for it in f["items"]: print(f"{it['cantidad']}x {it['nombre']} = {it['total']}")
        print(f"Subtotal:{f['subtotal']} | IVA:{f['iva']} | Total:{f['total']}")
    else: print("no encontrada")

def eliminar_factura():
    fid = int(input("ID de la factura que deseas eliminar "))
    fact = [f for f in cargar_facturas() if f["id"]!=fid]
    guardar_facturas(fact); print("eliminado")









def ejemplos_listas():#listas
    print("\n ULTIMOS 5 clientes en ganar el 50 % del mercado")
    listas = ["jose", "miguel", "ana", "luis", "maria", "carlos", "juan"]

    print(listas[5])  # imprimir por posicion
    print(listas[0])  # imprimir por posicion
    print(listas[2:5])
    for i in listas:
        print(i)

    listas2 = listas.copy()
    print(listas2)

    listas2 = listas[::-1]
    print(listas2)

    print(listas[-3])

    listas2 = [1, 2, 5, 7, 9, 8, 10, 12, 15, 20, 30]
    listas[6] = "pepe"
    print(listas)

    listas.append("pedro pablo")  # añadir datos
    print(listas)

    listas.insert(6, "natalia")  # insertar en una posicion especifica
    print(listas)

    listas.extend(["laura", "sofia", "andrea"])  # extender la lista
    print(listas)

    listas.remove("luis")  # remover un elemento
    print(listas)

    listas.pop(3)  # remover por posicion
    print(listas)

    for i in range(len(listas)):  # imprimir con indice
        print(i, ":", listas[i])

    lista3 = "polariose" in listas  # ver si un elemento esta en la lista
    print(lista3)

    lista3 = "pepe" in listas  # ver si un elemento esta en la lista
    print(lista3)

    listas4 = ["a", "a", "b", "b", "c", "c", "a"]
    cantidad = listas4.count("a")
    print(cantidad)

    cantidad = listas.count("natalia")  # contar elementos
    print(cantidad)

    listas.sort()  # ordenar lista
    print(listas)

    listas2 = listas.copy()
    listas2.sort()
    print(listas2)

    listas4.sort()
    print(listas4)

    listas6 = sorted(listas2)  # ordenar sin modificar la lista original
    print(listas6)

    listas6 = sorted(listas)
    print(listas6)

    listas.reverse()  # invertir lista
    print(listas)

    listas6 = listas.copy()  # copiar lista
    print(listas6)

    listas7 = list(listas)  # crea una listas copiada apartir de la lista original
    print(listas7)

    listas.clear()  # borrar todos los elementos
    print(listas)








def menu():#menu inicial
    while True:
        print("\n1.Inventario  2.Facturas  3.Promociones  0.Salir")
        op = input("Opción: ")
        if op=="1": menu_inv()
        elif op=="2": menu_fac()
        elif op=="3": ejemplos_listas()
        elif op=="0": break
        else: print("Opción no válida")

def menu_inv():
    ops = {"1":añadir_producto,"2":listar_productos,"3":buscar_producto,"4":eliminar_producto}
    print("\n1.Añadir 2.Listar 3.Buscar 4.Eliminar")
    ops.get(input("Opción: "), lambda:print(" Inválido"))()

def menu_fac():
    ops = {"1":crear_factura,"2":listar_facturas,"3":mostrar_factura,"4":eliminar_factura}
    print("\n1.Crear 2.Listar 3.Detalle 4.Eliminar")
    ops.get(input("Opción: "), lambda:print(" Inválido"))()

if __name__=="__main__":
    menu()