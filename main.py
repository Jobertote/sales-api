from app.services.sales_service import get_sales

def print_hi():
    ventas = get_sales()

    for venta in ventas:
        print(venta)

if __name__ == '__main__':
    print_hi()
