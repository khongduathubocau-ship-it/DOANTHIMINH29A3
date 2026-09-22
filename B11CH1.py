import math

print("\n--- Bài 11: Giải phương trình bậc hai ax^2 + bx + c = 0 ---")
a = float(input("Nhập hệ số a (a khác 0): "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Hệ số a phải khác 0. Vui lòng chạy lại chương trình.")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép x1 = x2 = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")