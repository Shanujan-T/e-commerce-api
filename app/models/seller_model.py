from app.extentions import db


class Seller(db.Model):
    __tablename__ = "sellers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )
    shop_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    user = db.relationship(
        "User",
        backref=db.backref("seller", uselist=False)
    )

    def __repr__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "shop_name": self.shop_name,
            "phone": self.phone,
            "address": self.address,
            "user": self.user,

        }
         