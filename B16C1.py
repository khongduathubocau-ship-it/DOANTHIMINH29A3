import math

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n (m > n): "))

# Tính UCLN bằng thuật toán Euclid
a, b = m, n
while b != 0:
    a, b = b, a % b
ucln = a

# Tính BCNN
bcnn = (m * n) // ucln

print(f"Ước chung lớn nhất của {m} và {n} là: {ucln}")
print(f"Bội chung nhỏ nhất của {m} và {n} là: {bcnn}")