from .extension import db

class Staff(db.Model):
    idNhanvien = db.Column(db.Integer, primary_key = True)
    tenNhanvien = db.Column(db.String(100), nullable = False)
    CCCD = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(100), unique = True)
    phone = db.Column(db.String(50), unique = True)

    def __init__(self, tenNhanvien, CCCD, email, phone):
        self.tenNhanvien = tenNhanvien
        self.CCCD = CCCD
        self.email = email
        self.phone = phone