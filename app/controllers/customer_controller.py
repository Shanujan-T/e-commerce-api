from datetime import datetime

from flask import jsonify, request

from app.extentions import db
from app.models.customer_model import Customer


def _validate_customer_payload(data, user_id=None):
    errors = []
    if not data:
        return ["Request body is required."]

    full_name = data.get("full_name")
    if full_name is None or str(full_name).strip() == "":
        errors.append("full_name is required.")

    address = data.get("address")
    if address is None or str(address).strip() == "":
        errors.append("address is required.")

    phone = data.get("phone")
    if phone is None or str(phone).strip() == "":
        errors.append("phone number is required.")

    return errors


def create_customer():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body is required."}), 400

    errors = _validate_customer_payload(data)
    if errors:
        return jsonify({"errors": errors}), 400


    try:
        customer = Customer(
            full_name=data.get("full_name").strip(),
            address=data.get("address").strip(),
        )
        db.session.add(customer)
        db.session.commit()
        return jsonify({"message": "customer created successfully.", "customer": customer.to_dict()}), 201
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500


def get_customers():
    customers = Customer.query.all()
    return jsonify({"customers": [s.to_dict() for s in customers]}), 200


def get_customer(user_id):
    customer = Customer.query.get(user_id)
    if not customer:
        return jsonify({"error": "customer not found."}), 404
    return jsonify({"customer": customer.to_dict()}), 200


def update_customer(user_id):
    customer = Customer.query.get(user_id)
    if not customer:
        return jsonify({"error": "customer not found."}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No data provided to update."}), 400

    errors = _validate_customer_payload(data, user_id=user_id)
    if errors:
        return jsonify({"errors": errors}), 400


    try:
        customer.full_name = data.get("full_name").strip()
        customer.address = data.get("address").strip()
        customer.phone = data.get("phone").strip()
        db.session.commit()
        return jsonify({"message": "customer updated successfully.", "customer": customer.to_dict()}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500


def delete_customer(user_id):
    customer = Customer.query.get(user_id)
    if not customer:
        return jsonify({"error": "customer not found."}), 404
    try:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({"message": "customer deleted successfully."}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500
