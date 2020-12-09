from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo

@app.route("/")
def home():

    # Find mars data
    mars_data = mongo.db.mars_data.find_one()
    
    
    # Return template and data
    return render_template("index.html", mars_data = mars_data)

# Route that will run 'scrape' function

@app.route("/scrape")
def Scrape():
    
    # Run script
    mars_data = scrape_mars.scrape_all()
    
     # Update the Mongo database using update and upsert=True
    mongo.db.mars_data.update({}, mars_data, upsert=True)
    
    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

    
    
