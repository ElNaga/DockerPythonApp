# Import the necessary modules
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# Define the endpoint
@app.route("/")
def hello():
    return "Hello from flask!"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)