"""This is a main file to start the application"""
import dotenv
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
def enable_cors(response):

    response.headers.add("Access-Control-Allow-Headers",
                         "authorization,content-type")
    response.headers.add("Access-Control-Allow-Methods",
                         "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':

    app.run()
