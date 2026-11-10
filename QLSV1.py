DSSV = []
def NhapDSSV():
    global DSSV
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập thông tin cho sinh viên thứ {i + 1}:")
        masv = input("Mã SV: ")
        tensv = input("Tên SV: ")
        gioitinh = input("Giới tính: ")
        toan = float(input("Điểm Toán: "))
        ly = float(input("Điểm Lý: "))
        hoa = float(input("Điểm Hóa: "))
        diemtb = (toan + ly + hoa) / 3

        sv = {
            "masv": masv,
            "tensv": tensv,
            "gioitinh": gioitinh,
            "toan": toan,
            "ly": ly,
            "hoa": hoa,
            "diemtb": diemtb
        }
        DSSV.append(sv)
    print("Đã nhập thành công danh sách sinh viên!")
def INDSSV():
    if not DSSV:
        print("Danh sách sinh viên trống!")
        return
    print("\n--- DANH SÁCH SINH VIÊN ---")
    print(f"{'Mã SV':<10} {'Họ Tên':<20} {'Giới Tính':<10} {'Toán':<6} {'Lý':<6} {'Hóa':<6} {'ĐTB':<6}")
    print("-" * 64)
    for sv in DSSV:
        print(
            f"{sv['masv']:<10} {sv['tensv']:<20} {sv['gioitinh']:<10} {sv['toan']:<6.2f} {sv['ly']:<6.2f} {sv['hoa']:<6.2f} {sv['diemtb']:<6.2f}")
def THEMSV():
    print("\n--- THÊM SINH VIÊN MỚI ---")
    masv = input("Mã SV: ")
    for sv in DSSV:
        if sv['masv'] == masv:
            print("Mã sinh viên đã tồn tại!")
            return
    tensv = input("Tên SV: ")
    gioitinh = input("Giới tính: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    diemtb = (toan + ly + hoa) / 3

    sv = {
        "masv": masv,
        "tensv": tensv,
        "gioitinh": gioitinh,
        "toan": toan,
        "ly": ly,
        "hoa": hoa,
        "diemtb": diemtb
    }
    DSSV.append(sv)
    print("Thêm sinh viên thành công!")
def XOASV():
    global DSSV
    masv = input("Nhập mã sinh viên cần xóa: ")
    found = False
    for sv in DSSV:
        if sv['masv'] == masv:
            DSSV.remove(sv)
            found = True
            print(f"Đã xóa sinh viên có mã {masv} thành công!")
            break
    if not found:
        print("Không tìm thấy sinh viên có mã này!")
def CAPNHATSV():
    masv = input("Nhập mã sinh viên cần cập nhật: ")
    found = False
    for sv in DSSV:
        if sv['masv'] == masv:
            found = True
            print(f"Đang cập nhật thông tin cho sinh viên: {sv['tensv']}")

            tensv = input("Tên mới (bỏ trống nếu giữ nguyên): ")
            if tensv.strip():
                sv['tensv'] = tensv

            gioitinh = input("Giới tính mới (bỏ trống nếu giữ nguyên): ")
            if gioitinh.strip():
                sv['gioitinh'] = gioitinh

            toan_str = input("Điểm Toán mới (bỏ trống nếu giữ nguyên): ")
            ly_str = input("Điểm Lý mới (bỏ trống nếu giữ nguyên): ")
            hoa_str = input("Điểm Hóa mới (bỏ trống nếu giữ nguyên): ")

            if toan_str.strip():
                sv['toan'] = float(toan_str)
            if ly_str.strip():
                sv['ly'] = float(ly_str)
            if hoa_str.strip():
                sv['hoa'] = float(hoa_str)

            # Tính lại điểm trung bình
            sv['diemtb'] = (sv['toan'] + sv['ly'] + sv['hoa']) / 3
            print("Cập nhật thông tin sinh viên thành công!")
            break

    if not found:
        print("Không tìm thấy sinh viên có mã này!")
def SAPXEP_DTB():
    if not DSSV:
        print("Danh sách trống!")
        return
    print("1. Sắp xếp Điểm TB tăng dần")
    print("2. Sắp xếp Điểm TB giảm dần")
    chon = input("Lựa chọn (1/2): ")
    if chon == '1':
        DSSV.sort(key=lambda x: x['diemtb'])
        print("Đã sắp xếp điểm TB tăng dần!")
    elif chon == '2':
        DSSV.sort(key=lambda x: x['diemtb'], reverse=True)
        print("Đã sắp xếp điểm TB giảm dần!")
    else:
        print("Lựa chọn không hợp lệ!")
    INDSSV()
def SAPXEP_TEN():
    if not DSSV:
        print("Danh sách trống!")
        return
    print("1. Sắp xếp tên A-Z")
    print("2. Sắp xếp tên Z-A")
    chon = input("Lựa chọn (1/2): ")
    if chon == '1':
        DSSV.sort(key=lambda x: x['tensv'])
        print("Đã sắp xếp theo tên từ A-Z!")
    elif chon == '2':
        DSSV.sort(key=lambda x: x['tensv'], reverse=True)
        print("Đã sắp xếp theo tên từ Z-A!")
    else:
        print("Lựa chọn không hợp lệ!")
    INDSSV()
def SAPXEP_MASV():
    if not DSSV:
        print("Danh sách trống!")
        return
    print("1. Sắp xếp mã SV tăng dần")
    print("2. Sắp xếp mã SV giảm dần")
    chon = input("Lựa chọn (1/2): ")
    if chon == '1':
        DSSV.sort(key=lambda x: x['masv'])
        print("Đã sắp xếp theo mã SV tăng dần!")
    elif chon == '2':
        DSSV.sort(key=lambda x: x['masv'], reverse=True)
        print("Đã sắp xếp theo mã SV giảm dần!")
    else:
        print("Lựa chọn không hợp lệ!")
    INDSSV()
def main():
    while True:
        print("\n================ CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ================")
        print("1. Nhập thông tin sinh viên")
        print("2. In danh sách sinh viên")
        print("3. Thêm thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Cập nhật thông tin sinh viên theo mã sinh viên")
        print("6. Sắp xếp sinh viên theo Điểm TB")
        print("7. Sắp xếp theo tên sinh viên")
        print("8. Sắp xếp sinh viên theo Mã SV")
        print("0. Nhập 0 để thoát")
        print("================================================================")

        chon = input("Chọn chức năng (0-8): ")
        if chon == '1':
            NhapDSSV()
        elif chon == '2':
            INDSSV()
        elif chon == '3':
            THEMSV()
        elif chon == '4':
            XOASV()
        elif chon == '5':
            CAPNHATSV()
        elif chon == '6':
            SAPXEP_DTB()
        elif chon == '7':
            SAPXEP_TEN()
        elif chon == '8':
            SAPXEP_MASV()
        elif chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 8.")
