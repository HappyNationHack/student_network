from flask import render_template

def extend_application(app):
    @app.route('/sign-in')
    def sign_handler():
        return render_template('sign-in.html')