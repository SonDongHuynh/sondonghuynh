from library.extension import db, mail
from requests import request
from library.staff_ma import StaffSchema
from library.model import Staff
from flask_mail import Mail, Message
from flask import request, jsonify
import json

staff_Schema = StaffSchema()
staffs_Schema = StaffSchema(many = True)

def add_staff_service():
    data = request.json
    staffs = Staff.query.with_entities(Staff.CCCD, Staff.email, Staff.phone)
    if (data and ('tenNhanvien' in data) and ('CCCD' in data)
        and ('email' in data) and ('phone' in data)):
        if (Staff.query.filter(Staff.CCCD == data["CCCD"]).first() or Staff.query.filter(Staff.email == data["email"]).first()
            or Staff.query.filter(Staff.phone == data["phone"]).first()):
            return "Can not add staff because CCCD or email or phone already exist"
        else:
            tenNhanvien = data["tenNhanvien"]
            CCCD = data["CCCD"]
            email = data["email"]
            phone = data["phone"]
            title_mail = "New staff"
            msg = Message(title_mail, sender='sondongh113@gmail.com', recipients=[email])
            message_email = "Congratulations {}, You have been successfully added to the staff!".format(tenNhanvien)
            msg.body = message_email
            try:
                mail.send(msg)
                new_staff = Staff(tenNhanvien, CCCD, email, phone)
                db.session.add(new_staff)
                db.session.commit()
                return "Add staff success "
            except IndentationError:
                db.session.rollback()
                return "Can not add staff"
    else:
        return "Request error"

def get_all_staff_service():
    staffs = Staff.query.with_entities(Staff.idNhanvien, Staff.tenNhanvien)
    if staffs:
        return staffs_Schema.jsonify(staffs)
    else:
        return "Not found staff"
def get_staff_by_id_service(id):
    staff = Staff.query.get(id)
    if staff:
        return staff_Schema.jsonify(staff)
    else:
        return "Not found staff"

def update_staff_by_id_service(id):
    staff = Staff.query.get(id)
    data = request.json
    if staff:
        if (data and ('tenNhanvien' in data) and ('CCCD' in data)
        and ('email' in data) and ('phone' in data)):
           
            try:
                staff.tenNhanvien = data["tenNhanvien"]
                staff.CCCD = data["CCCD"]
                staff.email = data["email"]
                staff.phone = data["phone"]
                db.session.commit()
                return staff_Schema.jsonify(staff)
            except IndentationError:
                    db.session.rollback()
                    return "Can not update staff!"
    else:
        return "Not found staff"

def delete_staff_by_id_service(id):
    staff = Staff.query.get(id)
    if staff:
        try:
            db.session.delete(staff)
            db.session.commit()
            return "Staff deleted!"
        except IndentationError:
            db.session.rollback()
            return "Can not delete staff!"
    else:
        return "Not found staff"