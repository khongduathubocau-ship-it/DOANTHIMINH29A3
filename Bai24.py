s = input("Nhập xâu ký tự: ")

so = 0
chu_hoa = 0
chu_thuong = 0
dac_biet = 0

for ky_tu in s:
    if ky_tu.isdigit():
        so += 1
    elif ky_tu.isupper():
        chu_hoa += 1
    elif ky_tu.islower():
        chu_thuong += 1
    else:
        dac_biet += 1

print("Số ký tự số:", so)
print("Số ký tự chữ in hoa:", chu_hoa)
print("Số ký tự chữ thường:", chu_thuong)
print("Số ký tự đặc biệt:", dac_biet)