from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import customer_controller as ctrl

customer_bp = Blueprint("", __name__, url_prefix="/api/customers")


@customer_bp.route("", methods=["POST"])
@jwt_required()
def create_customer():
    return ctrl.create_customer()



@customer_bp.route("", methods=["GET"])
@jwt_required()
def get_customers():
    return ctrl.get_customers()


@customer_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_customer(user_id):
    return ctrl.get_customer(user_id)


@customer_bp.route("/<int:user_id>", methods=["PUT"])
def update_customer(user_id):
    return ctrl.update_customer(user_id)


@customer_bp.route("/<int:user_id>", methods=["DELETE"])

def delete_customer(user_id):
    return ctrl.delete_customer(user_id)


