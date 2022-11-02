from flask import Flask
from flask_cors import CORS

from config import config

from routes import Movie

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "*"}})

def page_not_found(error):
    print(error)
    return error, 404

if __name__ == "__main__":
    app.config.from_object(config["development"])

    app.register_blueprint(Movie.main, url_prefix="/api/movies")

    app.register_error_handler(404, page_not_found)

    app.run()
