from flask import Flask, render_template

# 'flask run' automatically detects an app (app or application) or factory (create_app or make_app).
# create and configure the app

app = Flask(__name__)

from .main import main
app.register_blueprint(main)