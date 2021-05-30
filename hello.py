from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

#Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What`s Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

#Create Name Page

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("name.html", 
    name = name, 
    form = form)