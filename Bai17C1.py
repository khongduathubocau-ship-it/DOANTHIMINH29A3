# Số hoàn hảo là số nguyên dương có tổng các ước số dương (không kể chính nó) bằng chính nó.
n = int(input("Nhập số nguyên dương n: "))
tong_uoc = 0

for i in range(1, n):
    if n % i == 0:
        tong_uoc = tong_uoc + i

if tong_uoc == n:
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")