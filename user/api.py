from events.facade import Facade
from flask import render_template

def extend_application(app):
    @app.route('/my')
    def my_handler():
        return render_template('my-page.html')
