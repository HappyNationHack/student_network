from events.facade import Facade
from flask import render_template


def extend_application(app):
    @app.route('/events')
    def events_handler():
        Facade.get_event(1)
        return render_template('events.html')
