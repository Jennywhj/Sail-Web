from .blueprint import facility
from flask import render_template

@facility.route('/bruker-biospec-94-30')
def bruker_biospec_94_30():
    return render_template('facility/Bruker Biospec 94 30.html')