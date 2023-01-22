from flask import Flask
# Create a Flask instance
app = Flask(__name__)

# Define routes: Use the @app.route decorator to define routes for your application. A route is the URL path that a user will visit to access different parts of your application.
@app.route('/')
def hello_world():
    return 'Hello, World!'
#Start the development server: To start the development server, add the following line at the bottom of your app.py file:
if __name__ == '__main__':
    app.run(debug=True) # debug=True will reload the server every time you make a change to your code
    