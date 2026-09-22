# Tính tổng bình phương
n = int(input("Nhập số nguyên dương n: "))
tong_binh_phuong = 0
for i in range(1, n + 1,2):
        tong_binh_phuong = tong_binh_phuong + i * i
print(f"Tổng bình phương các số lẻ từ 1 đến {n} là: {tong_binh_phuong}")

# Dùng vòng lặp While
n = int(input("Nhập số nguyên dương n: "))
tong_binh_phuong = 0
i = 1  # Biến đếm bắt đầu từ 1

while i <= n:
    if i % 2 != 0:  # Kiểm tra số lẻ
        tong_binh_phuong = tong_binh_phuong + i * i
    i = i + 1  # Tăng biến đếm lên 1

print(f"Tổng bình phương các số lẻ từ 1 đến {n} là: {tong_binh_phuong}")
