from flask import Flask

# Initialize the web application
app = Flask(__name__)

# Define the homepage route
@app.route("/")
def home():
    return "Hello, World! Your Flask app is running."

# Run the local server
if __name__ == "__main__":
    app.run(debug=True)
