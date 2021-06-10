import os

from flask_wtf import CSRFProtect

from routes import app

if __name__ == "__main__":
    csrf = CSRFProtect(app)
    SECRET_KEY = os.urandom(32)
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['REMEMBER_COOKIE_HTTPONLY'] = True
    app.config['JSON_SORT_KEYS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY
    csrf.init_app(app)
    app.run(debug=True, port=8886, host='localhost')
