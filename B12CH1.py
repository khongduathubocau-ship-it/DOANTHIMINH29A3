import math

print("\n--- Bài 12: Kiểm tra điểm M có nằm trong hình tròn ---")
x = float(input("Nhập hoành độ điểm M (x): "))
y = float(input("Nhập tung độ điểm M (y): "))
a = float(input("Nhập hoành độ tâm I (a): "))
b = float(input("Nhập tung độ tâm I (b): "))
R = float(input("Nhập bán kính R: "))

# Tính khoảng cách từ M đến I
d = math.sqrt((x - a)**2 + (y - b)**2)

if d <= R:
    print("True")  # Nằm trong hoặc trên hình tròn
else:
    print("False") # Nằm ngoài hình tròn