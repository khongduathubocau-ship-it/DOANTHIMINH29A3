class Triple:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.S = (a+b+c)
    def Update(self):
        self.S = self.a + self.b + self.c
    def Change(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.S = self.a + self.b + self.c
    def isTriple(self):
        if (self.a > 0 and self.b > 0 and self.c > 0 and
            self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            return True
        return False
t = Triple(1, 2, 3)
print("Tổng ban đầu:", t.S)
t.Change(2,3,4)
print("Tổng sau:",t.S)
print("Có phải là tam giác không?:",t.isTriple())