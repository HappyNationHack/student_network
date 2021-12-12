from flask import Flask

import events.api as events_api
import user.api as user_api
import main_page.api as main_api
import sign_in.api as sign_api

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Up and running!'


events_api.extend_application(app)
user_api.extend_application(app)
main_api.extend_application(app)
sign_api.extend_application(app)
