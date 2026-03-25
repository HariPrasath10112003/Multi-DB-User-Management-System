from flask_cors import CORS
from flask import Flask

#import routes
from routes.register import register_bp
from routes.login import login_bp
from routes.profile import profile_bp

# main application
app = Flask(__name__)
CORS(app)

# register routes
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(profile_bp)

#run the app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)