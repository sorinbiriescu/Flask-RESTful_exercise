from flask import Blueprint, render_template
from logzero import logger


main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/")
@main_routes.route("/index")
def hello_world():
    logger.info("/")
    return render_template("index.html")

@main_routes.route("/examples")
def foundation_examples():
    logger.info("/examples")
    return render_template("examples.html")