from flask import Blueprint

from views import weather_view

webapp = Blueprint('webapp', __name__)


@webapp.get('/weather')
def weather_app_route():
    return weather_view()
