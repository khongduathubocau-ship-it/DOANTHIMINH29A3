def UCLN(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a # return b cũng được

def rutgon(tu,mau):
    tu1= tu
    tu = tu/UCLN(tu,mau)
    mau = mau/UCLN(tu1,mau)
    print(tu,'/',mau)
    
def cong(tu1, mau1, tu2, mau2):
    tu = tu1 * mau2 + mau1 * tu2
    mau = mau1 * mau2
    rutgon(tu, mau)

def tru(tu1, mau1, tu2, mau2):
    tu = tu1 * mau2 - mau1 * tu2
    mau = mau1 * mau2
    rutgon(tu, mau)

def nhan(tu1, mau1, tu2, mau2):
    tu = tu1 * tu2
    mau = mau1 * mau2
    rutgon(tu, mau)

def chia(tu1, mau1, tu2, mau2):
    tu = tu1 * mau2
    mau = mau1 * tu2
    rutgon(tu, mau)
cong(1,2,3,4)