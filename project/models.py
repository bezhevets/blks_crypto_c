from project.extensions import db


class Wallet(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    base58check_address: str = db.Column(db.String(255), nullable=False)
    hex_address: str = db.Column(db.String(255), nullable=False)
    private_key: str = db.Column(db.String(255), nullable=False)
    public_key: str = db.Column(db.String(255), nullable=False)
