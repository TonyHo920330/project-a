# db.py
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

mysql = None  # 將 mysql 實體設為全域變數

def init_db(app):
    global mysql
    # 載入 .env 檔案
    load_dotenv()

    # 設定資料庫參數
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # 讓 cursor 回傳 dict，而不是 tuple

    # 初始化 MySQL
    mysql = MySQL(app)
    return mysql
