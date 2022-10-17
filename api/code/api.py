from random import random
from flask import Flask
import os
import random

app = Flask(__name__)

meals = [
        {
            'name' : 'Paneer Tikka Masala',
            'Cuisine' : 'Indian',
            'Price' : '$19.99'
        },
        {
            'name' : 'Chole Bhature',
            'Cuisine' : 'Indian',
            'Price' : '$16.99'
        },
        {
            'name' : 'Rajma Chawal',
            'Cuisine' : 'Indian',
            'Price' : '$14.99'
        },
        {
            'name' : 'Aloo Muter',
            'Cuisine' : 'Indian',
            'Price' : '$15.99'
        },
        {
            'name' : 'Dal Tadka',
            'Cuisine' : 'Indian',
            'Price' : '$10.99'
        },
        {
            'name' : 'Shahi Paneer',
            'Cuisine' : 'Indian',
            'Price' : '$19.99'
        },
        {
            'name' : 'Arrabiatta Pasta',
            'Cuisine' : 'Italian',
            'Price' : '$17.99'
        },
        {
            'name' : 'Alfredo Pasta',
            'Cuisine' : 'Italian',
            'Price' : '$14.99'
        },
        {
            'name' : 'Enchiladas',
            'Cuisine' : 'Mexican',
            'Price' : '$10.99'
        },
        {
            'name' : 'Tacos',
            'Cuisine' : 'Mexican',
            'Price' : '$4.99'
        },
        {
            'name' : 'Burritos',
            'Cuisine' : 'Mexican',
            'Price' : '$4.99'
        },
        {
            'name' : 'Nachos',
            'Cuisine' : 'Mexican',
            'Price' : '$3.99'
        },
        {
            'name' : 'Italian Cheese Pizza',
            'Cuisine' : 'Italian',
            'Price' : '$14.99'
        },
        {
            'name' : 'Cheese Burger',
            'Cuisine' : 'American',
            'Price' : '$6.99'
        },
        {
            'name' : 'Fries',
            'Cuisine' : 'American',
            'Price' : '$3.99'
        }
    ]

# os.environ["API_ENDPOINT"]='meal'
# api_endpoint = os.environ.get("API_ENDPOINT")

@app.route('/')
def get_reco():
    random_choice = random.randint(0,15)
    return meals[random_choice]
    # return "Hello"

if __name__ == '__main__':
    port = os.environ.get('API_PORT', 5000)
    app.run(host='0.0.0.0',port=port)
 
 #Amey Darwhekar
 