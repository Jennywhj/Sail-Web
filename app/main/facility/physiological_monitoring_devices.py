from .blueprint import facility
from flask import render_template

@facility.route('/physiological-monitoring-devices')
def physiological_monitoring_devices():
    return render_template('facility/Physiological Monitoring Devices.html')