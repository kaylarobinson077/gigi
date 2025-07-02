from flask import Flask, jsonify
from ai_engine.core import gigi_router

app = Flask(__name__)

# Register AI assistant routes
app.register_blueprint(gigi_router, url_prefix="/gigi")


@app.route("/")
def index():
    return jsonify({"message": "Welcome to Gigi AI Assistant API"})


if __name__ == "__main__":
    app.run(debug=True)
