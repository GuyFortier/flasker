from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#    return "<h1>Hello World!<h1/>"
 
def index():
    first_name = "Guy"
    second_name = "Fortier"
    stuff = "This is <strong> Bold Text </strong>"
    favorite_pizza = ["Pepperoni","Cheese","Mushrooms","41"]

    return render_template("index.html", first_name=first_name, second_name=second_name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5000/user/Guy
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
