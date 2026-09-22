n = int(input("Nhập số nguyên dương n: "))
tong = 0
for i in range(1, n + 1):
    tong = tong + i
print(f"Tổng các số từ 1 đến {n} là: {tong}")

i=1
while i<=n:
    tong = tong + i
    i+i+1
print(f"Tổng các số từ 1 đến {n} là: {tong}")