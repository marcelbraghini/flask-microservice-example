from flask import Flask

from application.endpoint import history_action_controller, current_action_controller, status_controller


def create_app(config_name):

    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(history_action_controller.blueprint)

    app.register_blueprint(current_action_controller.blueprint)

    app.register_blueprint(status_controller.blueprint)

    return app
