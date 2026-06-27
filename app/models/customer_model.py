from app.extentions import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = db.Column(db.Integer, nullable=False )
    full_name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text())


    def to_dict(self):
        """Return a dictionary representation of the user."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name":self.full_name,
            "phone":self.phone,
            "address":self.address,
        }




