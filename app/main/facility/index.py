from .blueprint import facility
from flask import render_template

@facility.route('/')
def index():
    return render_template('facility/index.html')