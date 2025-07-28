from flask import Flask, session, redirect, request, jsonify
from config import config
from flask_cors import CORS
from dotenv import load_dotenv
from db import init_db
from routes.home import home_bp
from config.line import *
import os
import requests

# 載入 .env 環境變數
load_dotenv()

# 建立 Flask 應用
app = Flask(__name__)
app.config.from_object(config)

# 啟用 CORS（允許前端跨來源請求）
CORS(app)

mysql = init_db(app)  # ✅ 初始化資料庫連線
app.config['MYSQL'] = mysql  # 可選：保留給其他模組使用

@app.route("/", methods=["POST"])
def index():
    return 'OK', 200

# LINE Login 授權 URL
@app.route("/login")
def login():
    login_url = (
        f"https://access.line.me/oauth2/v2.1/authorize"
        f"?response_type=code&client_id={LINE_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=profile%20openid"
        f"&state=random_state_string"  # ✅ 建議之後用 session 存真正隨機值
    )
    return redirect(login_url)

# LINE 授權回傳
@app.route("/callback")
def callback():
    session.permanent = True
    code = request.args.get("code")
    if not code:
        return "未授權，請重新登入"

    token_url = "https://api.line.me/oauth2/v2.1/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": LINE_CLIENT_ID,
        "client_secret": LINE_CLIENT_SECRET,
    }
    response = requests.post(token_url, headers=headers, data=data).json()
    
    if "access_token" not in response:
        return f"授權失敗：{response}"

    access_token = response["access_token"]
    profile_url = "https://api.line.me/v2/profile"
    headers = {"Authorization": f"Bearer {access_token}"}
    profile = requests.get(profile_url, headers=headers).json()

    if "userId" not in profile or "displayName" not in profile:
        return "取得使用者資訊失敗"
    
    line_user_id = profile["userId"]
    display_name = profile["displayName"]
    picture_url = profile.get("pictureUrl", None)

    # ✅ 儲存到 session
    session["user_id"] = line_user_id
    session["display_name"] = display_name

    # ✅ 儲存到資料庫
    conn = app.config["MYSQL"].connection
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE line_user_id = %s", (line_user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        cursor.execute(
            "INSERT INTO users (line_user_id, display_name, picture_url) VALUES (%s, %s, %s)",
            (line_user_id, display_name, picture_url)
        )
        conn.commit()

    return redirect("/welcome")


@app.route("/api/me", methods=["GET"])
def get_user_info():
    user_id = session.get("user_id")
    display_name = session.get("display_name")

    if not user_id:
        return jsonify({"success": False, "message": "未登入"}), 401

    return jsonify({
        "success": True,
        "user": {
            "user_id": user_id,
            "display_name": display_name
        }
    })

# 註冊 Blueprint 路由
app.register_blueprint(home_bp)

# 主程式啟動
if __name__ == '__main__':
    app.run(debug=True)
