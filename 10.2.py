class NhanVien:
    def __init__(x, ten, thang, luongcb, snlv, hsl):
        x.ten = ten
        x.thang = thang
        x.luongcb = luongcb
        x.snlv = snlv 
        x.hsl = hsl
    
    def tinh_luong(x):
        luong_tong = x.luongcb * x.snlv * x.hsl - 1000000
        if(luong_tong > 9000000):
            luong_tong = 0.9 * luong_tong
            return luong_tong
        else:
            return luong_tong
        
    def hien_thi_luong(x):
        print("Lương của nhân viên {} nhận được trong tháng {} là: ".format(x.ten, x.thang) + str(x.tinh_luong()) + " VND")
"""
ten = str(input("Tên nhân viên: "))
thongtin = list(map(float, input("Thông tin: ").split()))
NhanVien(ten, thongtin[0], thongtin[1], thongtin[2], thongtin[3]).hien_thi_luong()
"""

class QuanLy(NhanVien):
    def __init__(x, ten, thang, luongcb, snlv, hsl, hshieuqua):
        super().__init__(ten, thang, luongcb, snlv, hsl)
        x.hshieuqua = hshieuqua
    
    def tinh_luong_thuong(x):
        if(x.hshieuqua < 1):
            return (x.tinh_luong() * x.hshieuqua)
        else:
            return (x.tinh_luong() + ((x.luongcb * x.snlv * x.hsl - 1000000) * (x.hshieuqua - 1) * 0.85))
    
    def hien_luong(x):
        print("Lương của nhân viên {} nhận được trong tháng {} là: ".format(x.ten, x.thang) + str(x.tinh_luong_thuong()) + " VND")


ten = str(input("Tên quản lý: ")).strip()
thongtin = list(map(float, input("Thông tin: ").split()))
QuanLy(ten, thongtin[0], thongtin[1], thongtin[2], thongtin[3], thongtin[4]).hien_luong()