"""This is a main file to start the application"""
import dotenv
from flask_cors import CORS
from configs import ConfigManager
from views.real_estate import real_estate_ns
from utils import create_app, add_namespaces, api
# -------------------------------------------------------------------------
dotenv.load_dotenv()
# ------------------------------------------------------------------------
config = ConfigManager().get_config()
app = create_app(config)
add_namespaces(api, [real_estate_ns])
cors = CORS(app, resources={
    r"/offers/*": {"origins": "https://skypro-raids-01-front.onrender.com"}})


if __name__ == '__main__':

    app.run()
