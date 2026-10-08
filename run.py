from flask import Flask
from app.routes.sales import sales_bp

app = Flask(__name__)

app.register_blueprint(sales_bp)

@app.route("/")
def home():
    return {"message": "Sales API is running"}

if __name__ == "__main__":
    app.run(debug=True)