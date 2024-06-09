from flask import Flask
import os
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    csrf = CSRFProtect(app)

    from .main import main
    from .auth import auth
    from .error import page_not_found

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_error_handler(404, page_not_found)

    return app
