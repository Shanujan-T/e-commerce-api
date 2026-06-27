from flask import Blueprint
from app.controllers import product_controller as ctrl

product_bp = Blueprint("products", __name__, url_prefix="/api/products")


@product_bp.route("", methods=["POST"])
def create_product():
    return ctrl.create_product()


@product_bp.route("", methods=["GET"])
def get_products():
    return ctrl.get_products()


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return ctrl.get_product(product_id)


@product_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    return ctrl.update_product(product_id)


@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    return ctrl.delete_product(product_id)