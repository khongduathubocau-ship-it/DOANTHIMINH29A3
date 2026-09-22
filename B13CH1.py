print("\n--- Bài 13: Kiểm tra loại tam giác ---")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Sử dụng epsilon để so sánh số thực an toàn hơn
eps = 1e-9

# 1. Kiểm tra điều kiện tạo thành tam giác
if (a + b > c) and (a + c > b) and (b + c > a):
    # 2. Kiểm tra các loại tam giác đặc biệt

    # Kiểm tra tam giác đều (3 cạnh bằng nhau)
    if abs(a - b) < eps and abs(b - c) < eps:
        print("Đây là tam giác đều.")

    # Kiểm tra tam giác vuông (Định lý Pytago)
    # Ta cần kiểm tra cả 3 trường hợp vì chưa biết cạnh nào là cạnh huyền
    elif abs(a * a + b * b - c * c) < eps or abs(a * a + c * c - b * b) < eps or abs(b * b + c * c - a * a) < eps:
        # Trong tam giác vuông, có thể là vuông cân
        if abs(a - b) < eps or abs(a - c) < eps or abs(b - c) < eps:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác vuông.")

    # Kiểm tra tam giác cân (2 cạnh bằng nhau)
    elif abs(a - b) < eps or abs(a - c) < eps or abs(b - c) < eps:
        print("Đây là tam giác cân.")

    # Nếu không thuộc các trường hợp trên
    else:
        print("Đây là tam giác thường.")

else:
    print("Ba số a, b, c không phải là độ dài 3 cạnh của một tam giác.")