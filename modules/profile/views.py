
import os
from flask import Blueprint, render_template, url_for, request, Markup

import pyperclip


profile = Blueprint('profile', __name__, template_folder='templates',
                     url_prefix='/profile')


@profile.route('/', methods=['GET'])
def index():
    title = 'Profile'
    return render_template('profile/index.html', title=title)
