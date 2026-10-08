from app.services.sales_service import get_sales,get_sale_by_id, create_sale, update_sale, delete_sale
from app.schemas.sales_schema import SaleSchema, SaleResponseSchema, MessageResponseSchema
from flask_smorest import Blueprint, abort

sales_bp = Blueprint("sales", __name__, description="Sales operations")

@sales_bp.route("/sales", methods=["GET"])
@sales_bp.response(200, SaleResponseSchema(many=True))
def get_sales_route():
    sales = get_sales()

    return sales

@sales_bp.route('/sales/<int:id>',methods=['GET'])
@sales_bp.response(200, SaleResponseSchema)
def get_sale(id):
    sale = get_sale_by_id(id)

    if sale is None:
        abort(404, message="Sale not found")

    return sale

@sales_bp.route("/sales",methods=["POST"])
@sales_bp.arguments(SaleSchema)
@sales_bp.response(201, MessageResponseSchema)
def create_sale_route(data):

    producto = data["producto"]
    categoria = data["categoria"]
    precio = data["precio"]
    cantidad = data["cantidad"]
    fecha = data["fecha"]

    result = create_sale(producto, categoria, precio, cantidad, fecha)

    if not isinstance(result, int):
        abort(400, message=result["error"])

    return {"message": "Sale created", "id": result}

@sales_bp.route("/sales/<int:id>",methods=["PUT"])
@sales_bp.arguments(SaleSchema)
@sales_bp.response(200, SaleResponseSchema)
def update_sale_route(data, id):
    sale = get_sale_by_id(id)
    if sale is None:
        abort(404, message="Sale not found")

    producto = data["producto"]
    categoria = data["categoria"]
    precio = data["precio"]
    cantidad = data["cantidad"]
    fecha = data["fecha"]

    result = update_sale(id, producto, categoria, precio, cantidad, fecha)

    if "error" in result:
        abort(400, message=result["error"])

    return result

@sales_bp.route("/sales/<int:id>",methods=["DELETE"])
def delete_sale_route(id):
    sale = get_sale_by_id(id)
    if sale is None:
        abort(404, message="Sale not found")

    delete_sale(id)

    return {"message": "Sale deleted"}, 200
