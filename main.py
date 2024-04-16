from flask import Flask,render_template
import random

uygulama = Flask(__name__)

@uygulama.route("/")
def anasayfa():
    return render_template("dgs.html")

uygulama.run(debug = True)
