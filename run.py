"""This is a main file to start the application"""
from configs import ConfigManager
from views.real_estate import real_estate_ns
from utils import create_app, add_namespaces, api
# -------------------------------------------------------------------------

config = ConfigManager().get_config()
app = create_app(config)
add_namespaces(api, [real_estate_ns])


if __name__ == '__main__':

    app.run()
