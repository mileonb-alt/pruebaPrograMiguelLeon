productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}


def unidades_categoria(categoria):
    categoria = categoria.lower()
    tot = 0
    for cod in productos:
        if productos[cod][1].lower() == categoria:
            tot = tot + stock[cod][1]
    print("El total de unidades disponibles es:", tot)


def busqueda_precio(p_min, p_max):
    res = []
    for cod in stock:
        precio = stock[cod][0]
        uni = stock[cod][1]
        if precio >= p_min and precio <= p_max and uni != 0:
            nom = productos[cod][0]
            res.append(nom + "--" + cod)

    res.sort()

    if len(res) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        print("Los productos encontrados son:", res)


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()
    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    else:
        return False


def val_txt(txt):
    if txt.strip() == "":
        return False
    return True


def val_peso(peso_kg):
    return peso_kg > 0


def val_precio(precio):
    return precio > 0


def val_uni(unidades):
    return unidades >= 0


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    codigo = codigo.upper()
    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True


def eliminar_producto(codigo):
    codigo = codigo.upper()
    if codigo in productos:
        del productos[codigo]
        del stock[codigo]
        return True
    else:
        return False


op = 0

while op != 6:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

    ent = input("Ingrese opción: ")

    try:
        op = int(ent)
    except ValueError:
        op = -1

    if op == 1:
        cat = input("Ingrese categoría a consultar: ")
        unidades_categoria(cat)

    elif op == 2:
        ok = False
        while not ok:
            try:
                pmin = int(input("Ingrese precio mínimo: "))
                pmax = int(input("Ingrese precio máximo: "))
                ok = True
            except ValueError:
                print("Debe ingresar valores enteros")

        if pmin >= 0 and pmax >= 0 and pmin <= pmax:
            busqueda_precio(pmin, pmax)
        else:
            print("Esos precios no sirven, revisa los valores")

    elif op == 3:
        resp = "s"
        while resp == "s":
            cod = input("Ingrese código del producto: ")
            nvo_p = int(input("Ingrese nuevo precio: "))
            r = actualizar_precio(cod, nvo_p)
            if r:
                print("Precio actualizado")
            else:
                print("El código no existe")
            resp = input("¿Desea actualizar otro precio (s/n)?: ")

    elif op == 4:
        cod = input("Ingrese código del producto: ")
        nom = input("Ingrese nombre: ")
        cat = input("Ingrese categoría: ")
        mca = input("Ingrese marca: ")
        peso = float(input("Ingrese peso (kg): "))
        imp_txt = input("¿Es importado? (s/n): ")
        cach_txt = input("¿Es para cachorro? (s/n): ")
        precio = int(input("Ingrese precio: "))
        uni = int(input("Ingrese unidades: "))

        imp = imp_txt == "s"
        cach = cach_txt == "s"

        cod_ok = val_txt(cod) and cod.upper() not in productos
        nom_ok = val_txt(nom)
        cat_ok = val_txt(cat)
        mca_ok = val_txt(mca)
        peso_ok = val_peso(peso)
        precio_ok = val_precio(precio)
        uni_ok = val_uni(uni)

        if not cod_ok:
            print("Ese código no sirve, está vacío o ya existe")
        elif not nom_ok:
            print("Falta el nombre")
        elif not cat_ok:
            print("Falta la categoría")
        elif not mca_ok:
            print("Falta la marca")
        elif not peso_ok:
            print("El peso tiene que ser mayor a 0")
        elif not precio_ok:
            print("El precio tiene que ser mayor a 0")
        elif not uni_ok:
            print("Las unidades no pueden ser negativas")
        else:
            se_agrego = agregar_producto(cod, nom, cat, mca, peso, imp, cach, precio, uni)
            if se_agrego:
                print("Producto agregado")
            else:
                print("El código ya existe")

    elif op == 5:
        cod = input("Ingrese código del producto: ")
        r = eliminar_producto(cod)
        if r:
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif op == 6:
        print("Programa finalizado.")

    else:
        print("Debe seleccionar una opción válida")