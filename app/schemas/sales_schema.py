from marshmallow import Schema, fields

class SaleSchema(Schema):
    producto = fields.String(required=True)
    categoria = fields.String(required=True)
    precio = fields.Float(required=True)
    cantidad = fields.Integer(required=True)
    fecha = fields.Date(required=True)

class SaleResponseSchema(Schema):
    id = fields.Integer(required=True)
    producto = fields.String(required=True)
    categoria = fields.String(required=True)
    precio = fields.Float(required=True)
    cantidad = fields.Integer(required=True)
    fecha = fields.Date(required=True)

class MessageResponseSchema(Schema):
    message = fields.String(required=True)
    id = fields.Integer(required=True)