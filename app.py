from flask import Flask, render_template

import string
from random import random, seed
import random

import requests

seed(1)
app = Flask(__name__)

def generateImage():
	response = requests.get('http://www.picsum.photos/120/80')
	return (response.url)

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
        "image": generateImage(),
    }

@app.route("/")
def photos():
    users = []
    for _ in range(100):
        users.append(generateUser())
    return render_template('index.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)
