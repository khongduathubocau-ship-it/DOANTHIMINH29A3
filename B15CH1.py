n = int(input("Nhập số nguyên dương n: "))
tong_binh_phuong = 0
for i in range(1, n + 1):
    if i % 2 != 0: # Kiểm tra số lẻ
        tong_binh_phuong = tong_binh_phuong + i * i
print(f"Tổng bình phương các số lẻ từ 1 đến {n} là: {tong_binh_phuong}")