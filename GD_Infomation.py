from django.db import models

# Model khai bao thong tin tai khoan
class TaiKhoan(models.Model):
    ten_tai_khoan = models.CharField(max_length=255)  # Ten tai khoan cua nguoi dung
    email = models.EmailField(unique=True)  # Dia chi email dang ky
    mat_khau = models.CharField(max_length=255)  # Mat khau cua tai khoan

    def __str__(self):
        return self.ten_tai_khoan

# Model khai bao thong tin thanh toan
class ThongTinThanhToan(models.Model):
    so_the = models.CharField(max_length=16)  # So the thanh toan
    ngay_het_han = models.DateField()  # Ngay het han cua the
    ma_bao_mat = models.CharField(max_length=3)  # Ma bao mat (CVC/CVV)

    def hien_thi_so_the_an_toan(self):
        # Chi hien thi 4 so cuoi cua the
        return f"**** **** **** {self.so_the[-4:]}"

# Model Designer ke thua tu TaiKhoan va quan he voi ThongTinThanhToan
class TaiKhoanDesigner(TaiKhoan):
    thong_tin_thanh_toan = models.OneToOneField(
        ThongTinThanhToan, 
        on_delete=models.CASCADE, 
        related_name='tai_khoan_designer'
    )

    def hien_thi_thong_tin(self):
        return {
            "ten_tai_khoan": self.ten_tai_khoan,
            "email": self.email,
            "so_the": self.thong_tin_thanh_toan.hien_thi_so_the_an_toan(),
            "ngay_het_han": self.thong_tin_thanh_toan.ngay_het_han,
        }

# Vi du su dung
if __name__ == "__main__":
    # Tao tai khoan designer voi thong tin mau (chi danh cho huong dan, su dung qua shell hoac admin site de quan ly thuc te)
    from django.utils.timezone import now

    thanh_toan = ThongTinThanhToan(
        so_the="1234567812345678",
        ngay_het_han=now().date(),
        ma_bao_mat="123"
    )
    thanh_toan.save()

    designer = TaiKhoanDesigner(
        ten_tai_khoan="Designer01",
        email="designer01@example.com",
        mat_khau="matkhau123",
        thong_tin_thanh_toan=thanh_toan
    )
    designer.save()

    # Hien thi thong tin chi tiet
    print(designer.hien_thi_thong_tin())
    print(designer.hien_thi_thong_tin())
