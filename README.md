# Flask　template

## url

[flask](https://flask.palletsprojects.com/en/1.1.x/)

[Bootstrap](https://getbootstrap.com/)

## install

```
python -m venv venv
. venv/Script/activarte

pip install -U pip

pip install Flask
pip install SQLAlchemy flask-sqlalchemy
```



## blueprint

```
# modules/blogform/views.py

import os
from flask import Blueprint, render_template, url_for, request, Markup

import pyperclip


blogform = Blueprint('blogform', __name__, template_folder='templates',
                     url_prefix='/blogform') # 変数 blogfomと@blogform が同じであること

@blogform.route('/', methods=["POST", "GET"])
def index():
    title = "blogform"
    return render_template('blogform/index.html', title=title)

# url_for('blogform.index') になる

# app.py
# from はディレクトリ名　+ ファイル名 (modules/blogform/views.py)importは 変数名
from modules.blogform.views import blogform
from modules.database.views import database

# blueprint の分割templates配下はその親ディレクトリを作りそこにhtmlファイルを入れる
# 親ファイルが　databaseの場合 templates/database/index.html
# render_template('dabase.html')
# url_for('database.index') このindexは　indexファイルではなくdatabaseの
# def index() 関数名変えた場合　def hoge() => url_for('database.hoge')

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

