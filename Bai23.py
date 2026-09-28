chuoi= input("Nhập chuỗi: ")
chuoichuanhoa=""
kt = True
while kt:
    vt= chuoi.find(" ")
    if vt==-1:
        kt=False
        break
    else:
        tu1=chuoi [0:vt:1].title()
        print(tu1)
        chuoichuanhoa+=tu1+""
        chuoi= chuoi[vt+1:len(chuoi):1].strip()
print(chuoi.title())
chuoichuanhoa+= chuoi.title()
print("Chuỗi đã chuẩn hóa:",chuoichuanhoa.strip())