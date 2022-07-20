from flask import Blueprint
from .services import (add_staff_service,get_all_staff_service,get_staff_by_id_service, update_staff_by_id_service, delete_staff_by_id_service)

staffs = Blueprint("staffs",__name__)

@staffs.route("/staff-management/staff", methods = ['POST'])
def add_staff():
    return add_staff_service()

@staffs.route("/staff-management/staffs", methods = ['GET'])
def get_all_staff():
    return get_all_staff_service()

@staffs.route("/staff-management/staff/<int:id>", methods = ['GET'])
def get_staff(id):
    return get_staff_by_id_service(id)

@staffs.route("/staff-management/staff/<int:id>", methods = ['PUT'])
def update_staff(id):
    return update_staff_by_id_service(id)

@staffs.route("/staff-management/staff/<int:id>", methods = ['DELETE'])
def delete_staff(id):
    return delete_staff_by_id_service(id)
