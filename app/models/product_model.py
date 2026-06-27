from app.extentions import db



class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Decimal, nullable=False)
    stock = db.Column(db.Integer)
    image = db.Column(db.String)
    is_active = db.Column(db.Boolean)

    


