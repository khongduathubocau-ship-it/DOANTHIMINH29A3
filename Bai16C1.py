import math

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n (m > n): "))

for i in range (1, m*n):
    if m%i == 0 and n%i == 0:
        ucln=i
print(ucln)

for i in range (1, m*n):
    if i%m==0 and i%n==0:
        bcnn=i
        break
print(bcnn)
