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
    cursor = connection.cursor()

    cursor.execute(consulta)

    resultados = cursor.fetchall()


    return resultados

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

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(consulta, (id,))
    resultado = cursor.fetchone()

    return resultado

def create_sale(producto, categoria, precio, cantidad, fecha):
    consulta = """
    INSERT INTO dbo.Ventas
        (producto, categoria, precio, cantidad, fecha)
        VALUES (?, ?, ?, ?, ?)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        consulta,
        (producto, categoria, precio, cantidad, fecha)
    )

    connection.commit()

def update_sale(id, producto, categoria, precio, cantidad, fecha):
    consulta = """
    UPDATE dbo.Ventas
    SET 
        producto = ?,
        categoria = ?,
        precio = ?,
        cantidad = ?,
        fecha = ?
    WHERE id = ?
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        consulta,
        (producto, categoria, precio, cantidad, fecha, id)
    )

    connection.commit()

def delete_sale(id):
    consulta = """
    DELETE FROM dbo.Ventas
    WHERE id = ?
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        consulta,
        (id,)
    )

    connection.commit()