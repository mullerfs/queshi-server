from gevent.pywsgi import WSGIServer
import os

from dotenv import load_dotenv
load_dotenv()


from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "dev")


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever() 