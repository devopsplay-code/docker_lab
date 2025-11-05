# We are importing Flask. Flask is used to create a small web server.
from flask import Flask

# Here we are creating the web app object.
app = Flask(__name__)

# This tells Flask: when someone opens the website at "/", run the function below.
@app.get("/")
def home():
    # This is the text that will be shown in the browser.
    return "Hello Docker + Python"

# This line means: only start the server if we run this file directly.
if __name__ == "__main__":
    # Start the web server and allow access from outside the container.
    app.run(host="0.0.0.0")
