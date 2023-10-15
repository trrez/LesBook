from flask import Flask


app = Flask(__name__)
app.secret_key = "clave secreta"
BASE_DE_DATOS = "books"