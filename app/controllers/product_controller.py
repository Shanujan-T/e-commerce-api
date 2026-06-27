from datetime import datetime

from flask import jsonify, request

from app.extentions import db
from app.models.product_model import Product



def _validate_product_payload(data, id=None):
    errors = []
    if not data:
        return ["Request body is required."]

    full_name = data.get("full_name")
    if full_name is None or str(full_name).strip() == "":
        errors.append("full_name is required.")

    price = data.get("price")
    if price is None:
        errors.append("price is required.")
    else:
        try:
            price_val = int(price)
            if price_val <= 0:
                errors.append("price must be a positive integer.")
        except (TypeError, ValueError):
            errors.append("price must be a positive integer.")

    joined_raw = data.get("joined_date")
    if joined_raw is None or str(joined_raw).strip() == "":
        errors.append("joined_date is required.")

    return errors


def create_product():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body is required."}), 400

    errors = _validate_product_payload(data)
    if errors:
        return jsonify({"errors": errors}), 400


    try:
        product = Product(
            name=data.get("name").strip(),
            description=data.get("description").strip(),
            price=int(data.get("price")),
            stock=float(data.get("stock", 0.0)),
            image=data.get("image", True),
            is_active = is_active,
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product created successfully.", "product": product.to_dict()}), 201
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500


def get_products():
    products = Product.query.all()
    return jsonify({"products": [s.to_dict() for s in products]}), 200


def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found."}), 404
    return jsonify({"product": product.to_dict()}), 200


def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found."}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No data provided to update."}), 400

    errors = _validate_product_payload(data, product_id=product_id)
    if errors:
        return jsonify({"errors": errors}), 400


    try:
        product.name = data.get("name").strip()
        product.description = data.get("description").strip()
        product.price = int(data.get("price"))
        product.stock = int(data.get("stock"))
        product.image = data.get("image").strip()
        if "is_active" in data:
            product.is_active = bool(data.get("is_active"))
        db.session.commit()
        return jsonify({"message": "product updated successfully.", "product": product.to_dict()}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500


def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "product not found."}), 404
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully."}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500
