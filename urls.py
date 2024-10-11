from flask import Blueprint

from views import weather_view
from flask_cors import CORS

webapp = Blueprint('webapp', __name__)
CORS(webapp)


@webapp.get('/weather')
def weather_app_route():
    return weather_view()
