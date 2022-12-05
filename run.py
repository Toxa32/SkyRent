"""This is a main file to start the application"""
import dotenv
from flask import request, make_response
from configs import ConfigManager
from views.real_estate import real_estate_ns
from utils import create_app, add_namespaces, api
# -------------------------------------------------------------------------
dotenv.load_dotenv()
# ------------------------------------------------------------------------
config = ConfigManager().get_config()
app = create_app(config)
add_namespaces(api, [real_estate_ns])


@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response


if __name__ == '__main__':

    app.run()
