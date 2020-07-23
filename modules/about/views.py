import os
from flask import Blueprint, render_template, url_for, request, Markup



about = Blueprint('about', __name__, template_folder='templates',
                     url_prefix='/about')


@about.route('/', methods=['GET'])
def index():
    title = 'about'
    return render_template('about/index.html', title=title)
