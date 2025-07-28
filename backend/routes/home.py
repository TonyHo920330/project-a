from flask import Blueprint, jsonify, current_app

home_bp = Blueprint('home', __name__)

@home_bp.route("/api/home", methods=["GET"])
def home_data():
    mysql = current_app.config['MYSQL']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name FROM users LIMIT 1")
    result = cursor.fetchone()

    return jsonify({
        "user": {"name": result['name'] if result else '未知使用者'},
        "stats": {"users": 128, "posts": 84},
        "news": [
            {"title": "系統維護通知", "date": "2025-07-17"},
            {"title": "新版功能上線", "date": "2025-07-15"}
        ]
    })
