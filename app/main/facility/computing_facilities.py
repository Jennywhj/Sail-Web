from .blueprint import facility
from flask import render_template

@facility.route('/computing-facilities')
def computing_facilities():
    return render_template('facility/Computing Facilities.html')