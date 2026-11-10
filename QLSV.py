DSSV = []
def NhapDSSV(dssv):
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập sinh viên thứ {i + 1}:")
        masv = input("Mã sinh viên: ")
        hoten = input("Họ tên: ")
        toan = int(input("Toán: "))
        ly = int(input("Lý: "))
        hoa = int(input("Hóa: "))
        diemtb = (toan + ly + hoa) / 3

        if diemtb >= 8:
            xeploai = 'Gioi'
        elif diemtb >= 6.5:
            xeploai = 'Khá'
        elif diemtb >= 5:
            xeploai = 'Trung bình'
        else:
            xeploai = 'Yếu'

        sv = {
            'Mã SV': masv,
            'Họ tên': hoten,
            'Điểm Toán': toan,
            'Điểm Lý': ly,
            'Điểm Hóa': hoa,
            'Điểm TB': diemtb,
            'Xếp loại': xeploai
        }
        dssv.append(sv)
def INDSSV():
    for sv in DSSV:
        print(
            f"Mã SV: {sv.get('Mã SV'):<8} | Họ tên: {sv.get('Họ tên'):<18} | Toán: {sv.get('Điểm Toán'):<3} | Lý: {sv.get('Điểm Lý'):<3} | Hóa: {sv.get('Điểm Hóa'):<3} | ĐTB: {sv.get('Điểm TB'):<5.2f} | Xếp loại: {sv.get('Xếp loại')}")

def THEMSV():