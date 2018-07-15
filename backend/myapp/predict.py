import json
import os

def predict (name):
    model = json.load (open (os.path.join (os.path.dirname(os.path.abspath(__file__)), "classificator.json")))
    cats = json.load (open (os.path.join (os.path.dirname(os.path.abspath(__file__)), "categories.json")))
    numerical_cat = model[name]
    return cats[numerical_cat]