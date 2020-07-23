import os
from flask import Blueprint, render_template, url_for, request, Markup

# modules  はディレクトリ名 importはファイル名
from modules.about.views import about
from modules.profile.views import profile


app = Flask(__name__)


app.register_blueprint(about)

app.register_blueprint(profile)


@app.route("/")
def index():
    title = 'Top Page'
    return render_template("index.html", title=title)
