# The entry point where our Flask application is created and the server started.
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run()
