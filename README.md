# Flask Starter Template

## url

[flask](https://flask.palletsprojects.com/en/1.1.x/)

[Bootstrap](https://getbootstrap.com/)

## install

```
# start venv

python -m venv venv
. venv/Script/activarte

# module install
pip install -U pip

pip install Flask
pip install SQLAlchemy flask-sqlalchemy


# start server

python run.py

# browser

localhost:8888

# stop server
## keybord

ctrl + c

# stop venv

deactivate

```




## blueprint

```
# modules/blogform/views.py

import os
from flask import Blueprint, render_template, url_for, request, Markup


about = Blueprint('about', __name__, template_folder='templates',
                     url_prefix='/about') # 変数 blogfomと@blogform が同じであること

@about.route('/', methods=["POST", "GET"])
def index():
    title = "about"
    return render_template('about/index.html', title=title)

# link   url_for('about.index')

# app.py
# from dedirectory　+ fielname (modules/blogform/views.py) import は variable
from modules.blogform.views import blogform
from modules.database.views import database

# blueprint の分割templates配下はその親ディレクトリを作りそこにhtmlファイルを入れる
# 親ファイルが　aboutの場合 templates/about/index.html
# render_template('about/index.html')
# url_for('about.index') このindexは　indexファイルではなくblueprintの index()
# def index() 関数名変えた場合　def hoge() => url_for('hoge.hoge')

```

## git cmd

- merge

```
# commit 終了あと

git status

# On branch developer
# nothing to commit, working tree clean

git checkout

git checkout master

git merge

```

- マージで衝突が発生した場合

```
git add hello.html
git commit -m "hello.html衝突を修正"

```

- マージを元に戻す方法

```
マージした後、未だコミットしていない場合

git reset --hard HEAD

マージした後、コミットも行っている場合

git reset --hard ORIG_HEAD

```
- git branch

```
git branch -d <branchname>
-d、もしくは、--deleteオプション。
指定したブランチを削除する。
-rオプションを付けた場合は、リモートブランチを削除する。
指定したブランチの内容が、追跡しているリモートブランチ(設定されていない場合はHEAD)にマージされていないと削除できない。

git branch -D <branchname>
-Dオプション。
マージの状態に関わらず、指定したブランチを削除する。
```

