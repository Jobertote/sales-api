from app.database.connection import get_connection

def get_all_sales():
    consulta = """
    SELECT
        id,
        producto,
        categoria,
        precio,
        cantidad,
        fecha
    FROM dbo.Ventas
    ORDER BY id;
    """

    connection = get_connection()
    try:
        cursor = connection.cursor()

        cursor.execute(consulta)

        resultados = cursor.fetchall()

        return resultados
    finally:
        cursor.close()
        connection.close()

def get_sales_by_id(id):
    consulta = """
    SELECT
        id,
        producto,
        categoria,
        precio,
        cantidad,
        fecha
    FROM dbo.Ventas
    WHERE id = ?
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(consulta, (id,))
        resultado = cursor.fetchone()

        return resultado
    finally:
        cursor.close()
        connection.close()

def create_sale(producto, categoria, precio, cantidad, fecha):
    consulta = """
    INSERT INTO dbo.Ventas
        (producto, categoria, precio, cantidad, fecha)
    OUTPUT INSERTED.id
    VALUES (?, ?, ?, ?, ?)
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            consulta,
            (producto, categoria, precio, cantidad, fecha)
        )

        sale_id = cursor.fetchone()[0]

        connection.commit()

        return sale_id
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()



def update_sale(id, producto, categoria, precio, cantidad, fecha):
    consulta = """
    UPDATE dbo.Ventas
    SET 
        producto = ?,
        categoria = ?,
        precio = ?,
        cantidad = ?,
        fecha = ?
    OUTPUT INSERTED.*
    WHERE id = ?
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            consulta,
            (producto, categoria, precio, cantidad, fecha, id)
        )

        updated_sale = cursor.fetchone()

        sale = {
            "id": updated_sale[0],
            "producto": updated_sale[1],
            "categoria": updated_sale[2],
            "precio": updated_sale[3],
            "cantidad": updated_sale[4],
            "fecha": updated_sale[5]
        }

        connection.commit()

        return sale
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()

def delete_sale(id):
    consulta = """
    DELETE FROM dbo.Ventas
    WHERE id = ?
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            consulta,
            (id,)
        )

        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()