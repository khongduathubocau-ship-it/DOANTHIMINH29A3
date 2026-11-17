class HOCSINH:
    def __init__(self,hoten="",diachi="",chieucao=0.0,cannang=0.0):
        self.Hoten = hoten
        self.Diachi = diachi
        self.Chieucao = chieucao
        self.Cannang = cannang
    def nhap(self): #Nhập thông tin học sinh từ bàn phím
        print("Nhập thông tin học sinh: ")
        self.Hoten = input("Nhập họ tên:")
        self.Diachi = input("Nhập địa chỉ:")
        self.Chieucao = float(input("Nhập chiều cao:"))
        self.Cannang = float(input("Nhập cân nặng:"))
    def xuat(self): #Xem thông tin học sinh
        print("Thông tin học sinh:")
        print(f"Họ tên:{self.Hoten}")
        print(f"Địa chỉ:{self.Diachi}")
        print(f"Chiều cao:{self.Chieucao} cm")
        print(f"Cân nặng:{self.Cannang} kg")
    def capnhat(self,hoten=None,diachi=None,chieucao=None,cannang=None):
        if hoten is not None:
            self.Hoten = hoten
        if diachi is not None:
            self.Diachi = diachi
        if chieucao is not None:
            self.Chieucao = chieucao
        if cannang is not None:
            self.Cannang = cannang
hs1=HOCSINH("Nguyễn Văn A","Số nhà A, Ngõ B, Khu phố C, Đường D, Quận E, TP.F",170,55)
print("TRƯỚC KHI CẬP NHẬT")
hs1.xuat()
hs1.capnhat(hoten="Nguyễn Văn M")
print("SAU KHI CẬP NHẬT")
hs1.xuat()

