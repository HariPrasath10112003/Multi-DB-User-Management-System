from flask import Blueprint, request, jsonify
from db import mysql_conn, r

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    cursor = mysql_conn.cursor()

    query = "SELECT id FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    if user:
        user_id = user["id"]

        #store session in Redis
        r.set(f"session_{user_id}", email)

        return jsonify({
            "message": "Login Success",
            "user_id": user_id,
            "email": email
        })
    else:
        return jsonify({"message": "Invalid Credentials"}), 401