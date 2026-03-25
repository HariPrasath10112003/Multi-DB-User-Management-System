
from flask import Blueprint, request, jsonify
from db import profile_collection

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["POST"])
def profile():
    data = request.json

    email = data.get("email")
    age = data.get("age")
    dob = data.get("dob")
    contact = data.get("contact")
   #update in mongodb if email matches
    profile_collection.update_one(
        {"email": email},
        {
            "$set": {
                "age": age,
                "dob": dob,
                "contact": contact
            }
        },
        upsert=True #if there is no document, it will create
    )

    return jsonify({"message": "Profile Updated"})