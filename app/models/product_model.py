from app.extentions import db
from app.utils import utc_now
from werkzeug.security import generate_password_hash, check_password_hash


class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Decimal, nullable=False)
    stock = db.Column(db.Integer)
    image = db.Column(db.String)
    

    
    def to_dict(self):
        """Return a dictionary representation of the user."""
        return {
            "product_id": self.product_idid,
            "seller_id": self.seller_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "image": self.image,
            "is_active": self.is_active,
        }


