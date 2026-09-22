# Đếm các số nguyên tố nhỏ hơn n
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n: "))
dem = 0

for i in range(2, n):
    if la_so_nguyen_to(i):
        dem += 1

print(f"Số lượng số nguyên tố nhỏ hơn {n} là: {dem}")