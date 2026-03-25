from flask import Blueprint, request, jsonify
from db import mysql_conn

register_bp = Blueprint("register", __name__)

#Register endpoint
#accepting request from post 
@register_bp.route("/register", methods=["POST"])
def register():
    #receive json data from frontend 
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    #create mysql cursor
    cursor = mysql_conn.cursor()
    
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, password))
    mysql_conn.commit()

    return jsonify({"message": "User Registered Successfully"})