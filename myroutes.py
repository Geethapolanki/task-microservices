from ast import Num
import random
from config import app

@app.get('/message')
def fun():
    return "this is sample page"

@app.get('/number')
def fun():
    Num = random.randint(0,100)
    return f"{Num} is returned"

