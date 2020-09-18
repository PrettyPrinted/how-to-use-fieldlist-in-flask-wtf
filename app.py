# app.py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FieldList, IntegerField, Form
from wtforms.validators import Optional
from collections import namedtuple

app = Flask(__name__)
app.config['SECRET_KEY'] = 'keepthissecret'

class ProductForm(Form):
    title = StringField('Title')
    price = IntegerField('Price', validators=[Optional()])

class InventoryForm(FlaskForm):
    category_name = StringField('Category Name')
    products = FieldList(FormField(ProductForm), min_entries=4, max_entries=8)

@app.route('/', methods=['GET', 'POST'])
def index():
    product = namedtuple('Product', ['title', 'price'])

    data = {
        'category_name' : 'Widgets',
        'products' : [
            product('Unit 1', 100),
            product('Unit 2', 50),
            product('Unit 3', 20),
            product('Unit 4', 80),
            product('Unit 5', 10),
            product('Unit 6', 80),
            product('Unit 7', 150),
            product('Unit 8', 10),
        ]
    }
    form = InventoryForm(data=data)
    if form.validate_on_submit():
        for value in form.products.data:
            print(value)

        for field in form.products:
            print(field.title.data)
            print(field.price.data)

    return render_template('index.html', form=form)