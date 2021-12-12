from events.facade import Facade
from flask import render_template


def extend_application(app):
    @app.route('/')
    def main_handler():
        return render_template('main.html')