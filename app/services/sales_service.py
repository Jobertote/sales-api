from app.repositories.sales_repository import get_all_sales, get_sales_by_id, create_sale as create_sale_repository, update_sale as update_sale_repository, delete_sale as delete_sale_repository

def validate_sale(producto, categoria, precio, cantidad, fecha):
    categorias_validas = ["Tecnologia", "Muebles", "Oficina"]

    if not isinstance(precio, (int, float)):
        return {"error": "Price must be a number"}

    if precio <= 0:
        return {"error": "Price must be greater than zero"}

    if not isinstance(cantidad, int):
        return {"error": "Count must be a number"}

    if cantidad <= 0:
        return {"error": "Count must be greater than zero"}

    if not isinstance(producto, str):
        return {"error": "Producto must be a string"}

    if producto.strip() == "":
        return {"error": "Producto cannot be empty"}

    if not isinstance(categoria, str):
        return {"error": "Category must be a string"}

    if categoria not in categorias_validas:
        return {"error": "Invalid category"}


    return None

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
    result = validate_sale(
        producto,
        categoria,
        precio,
        cantidad,
        fecha
    )

    if result:
        return result

    try:
        id_sale = create_sale_repository(producto, categoria, precio, cantidad, fecha)

        return id_sale
    except Exception:
        raise

def update_sale(id, producto, categoria, precio, cantidad, fecha):
    result = validate_sale(
        producto,
        categoria,
        precio,
        cantidad,
        fecha
    )

    if result:
        return result

    try:
        updated_sale = update_sale_repository(id, producto, categoria, precio, cantidad, fecha)

        return updated_sale
    except Exception:
        raise

def delete_sale(id):
    try:
        delete_sale_repository(id)

        return None
    except Exception:
        raise
