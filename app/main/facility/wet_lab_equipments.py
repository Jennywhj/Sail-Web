from .blueprint import facility
from flask import render_template

@facility.route('/wet-lab-equipments')
def wet_lab_equipments():
    return render_template('facility/Wet Lab Equipments.html')