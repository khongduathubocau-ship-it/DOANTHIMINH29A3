def ptthuasonguyento(so):
    n = 2
    dsts = []
    while so > 1:
        if so % n == 0:
            dsts.append(n)
            so = so // n
        else:
            n += 1
    return dsts

so = int(input("Nhập số cần phân tích: "))
print(ptthuasonguyento())

