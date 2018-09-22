import os
from app.main import create_app

script_path = os.path.dirname(os.path.abspath( __file__ ))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.config.from_pyfile('development.cfg', silent=True)
    app.run(host="0.0.0.0", port=port)