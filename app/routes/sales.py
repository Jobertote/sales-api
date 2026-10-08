from app.services.sales_service import get_sales,get_sale_by_id, create_sale, update_sale, delete_sale
from flask import Blueprint, jsonify, request

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/sales", methods=["GET"])
def get_sales_route():
    sales = get_sales()

    return jsonify(sales)

@sales_bp.route('/sales/<int:id>',methods=['GET'])
def get_sale(id):
    sale = get_sale_by_id(id)

    if sale is None:
        return {"error": "Sale not found"}, 404

    return jsonify(sale), 200

@sales_bp.route("/sales",methods=["POST"])
def create_sale_route():
    data = request.get_json()
    if data is None:
        return {"error": "No data"}, 400

    producto = data.get("producto")
    categoria = data.get("categoria")
    precio = data.get("precio")
    cantidad = data.get("cantidad")
    fecha = data.get("fecha")

    if producto is None or categoria is None or precio is None or cantidad is None or fecha is None:
        return {"error": "Incomplete data"}, 400

    result = create_sale(producto, categoria, precio, cantidad, fecha)

    if result:
        return jsonify(result), 400

    return jsonify({"message": "Sale created"}), 201

@sales_bp.route("/sales/<int:id>",methods=["PUT"])
def update_sale_route(id):
    sale = get_sale_by_id(id)
    if sale is None:
        return {"error": "Sale not exist"}, 404

    data = request.get_json()
    producto = data.get("producto")
    categoria = data.get("categoria")
    precio = data.get("precio")
    cantidad = data.get("cantidad")
    fecha = data.get("fecha")
    if producto is None or categoria is None or precio is None or cantidad is None or fecha is None:
        return {"error": "Incomplete data"}, 400

    result = update_sale(id, producto, categoria, precio, cantidad, fecha)

    if result:
        return jsonify(result), 200

    return jsonify({"message": "Sale updated"}), 200

@sales_bp.route("/sales/<int:id>",methods=["DELETE"])
def delete_sale_route(id):
    sale = get_sale_by_id(id)
    if sale is None:
        return {"error": "Sale not exist"}, 404

    result = delete_sale(id)
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Sale deleted"}), 200