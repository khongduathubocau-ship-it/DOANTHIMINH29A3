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
t = Triple(1, 2, 3)
print("Tổng ban đầu:", t.S)
t.Change(2,3,4)
print("Tổng sau:",t.S)