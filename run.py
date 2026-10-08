from flask import Flask
from app.routes.sales import sales_bp
import logging
from flask_smorest import Api

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

app.config["API_TITLE"] = "Sales API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_JSON_PATH"] = "openapi.json"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)


@app.errorhandler(Exception)
def handle_exception(error):
    logger.exception("Unhandled exception")
    return {"error": "Internal Server Error"}, 500

api.register_blueprint(sales_bp)

@app.route("/")
def home():
    return {"message": "Sales API is running"}

if __name__ == "__main__":
    app.run(debug=True)