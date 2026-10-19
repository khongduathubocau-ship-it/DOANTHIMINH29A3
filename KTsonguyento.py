import math

# Nhập số n từ bàn phím
n = int(input("Nhập vào số tự nhiên n: "))

# Giả định ban đầu n là số nguyên tố
kt = True

# Kiểm tra các điều kiện cơ bản
if n < 2:
    kt = False
else:
    # Duyệt từ 2 đến căn bậc hai của n
    m = int(math.isqrt(n))
    for i in range(2, m + 1):
        if n % i == 0:
            kt = False
            break # Thoát vòng lặp ngay khi tìm thấy ước số

# In kết quả dựa vào biến cờ (flag)
if kt:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")