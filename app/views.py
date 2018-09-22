from flask import Blueprint
from logzero import logger


main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/")
def hello_world():
    logger.info("/")
    return "Hello World"