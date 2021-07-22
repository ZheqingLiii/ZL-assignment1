from types import resolve_bases
from flask import Flask, render_template

import string
import json
from random import random, seed
import random

import requests

seed(1)
app = Flask(__name__)

users = []

def generateImage():
    response = requests.get('http://www.picsum.photos/120/80')
    
    return (response.url)

def generateImages():
    response = requests.get('https://picsum.photos/v2/list?limit=100')
    response = json.loads(response.content)
    return response

def generateUser():
    letters = string.ascii_lowercase
    digits = string.digits[1:] # eliminate 0
    descriptions = string.ascii_lowercase + " ,."

    name = ''.join(random.choice(letters) for i in range(8))
    age = ''.join(random.choice(digits) for i in range(2))
    desp = ''.join(random.choice(descriptions) for i in range(15))

    return {
        "name": string.capwords(name),
        "age": age,
        "description": string.capwords(desp),
        # "image": generateImage(),
    }

@app.route("/age")
def orderByAge():
    return render_template('index.html', users=sorted(users, key=lambda k: k['age']))

@app.route("/name")
def orderByName():
    return render_template('index.html', users=sorted(users, key=lambda k: k['name']))

@app.route("/")
def photos():
    if len(users) < 100:
        images = generateImages()
        for i in range(100):
            user = generateUser()
            user["image"] = images[i]["download_url"]
            users.append(user)
    return render_template('index.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)
