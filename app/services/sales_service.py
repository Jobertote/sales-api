from app.repositories.sales_repository import get_all_sales, get_sales_by_id, create_sale as create_sale_repository, update_sale as update_sale_repository, delete_sale as delete_sale_repository

def get_sales():

    resultados = get_all_sales()
    array = []

    for sale in resultados:
        venta = {
            'id': sale[0],
            'producto': sale[1],
            'categoria': sale[2],
            'precio': float(sale[3]),
            'cantidad': sale[4],
            'fecha': sale[5],
        }

        array.append(venta)

    return array


def get_sale_by_id(id):
    sale = get_sales_by_id(id)

    if sale is None:
        return None

    venta = {
        'id': sale[0],
        'producto': sale[1],
        'categoria': sale[2],
        'precio': float(sale[3]),
        'cantidad': sale[4],
        'fecha': sale[5],
    }

    return venta

def create_sale(producto, categoria, precio, cantidad, fecha):
    if precio <= 0:
        return {"error": "Price must be greater than zero"}

    if cantidad <= 0:
        return {"error": "Count must be greater than zero"}


    create_sale_repository(producto, categoria, precio, cantidad, fecha)

    return None

def update_sale(id, producto, categoria, precio, cantidad, fecha):
    if precio <= 0:
        return {"error": "Price must be greater than zero"}
    if cantidad <= 0:
        return {"error": "Count must be greater than zero"}

    update_sale_repository(id, producto, categoria, precio, cantidad, fecha)

    return None

def delete_sale(id):
    delete_sale_repository(id)

    return None

