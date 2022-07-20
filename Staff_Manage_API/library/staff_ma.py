from .extension import ma 

class StaffSchema(ma.Schema):
    class Meta:
        fields = ('idNhanvien', 'tenNhanvien', 'CCCD', 'email', 'phone')