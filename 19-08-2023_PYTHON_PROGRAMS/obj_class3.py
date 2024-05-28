class A:
    def m1(self):
        print("method m1 in class A")
class B:
    def m2(self):
        print("method m2 in class B")
class C(B,A):
    def m3(self):
        print("method m3 in class C")
obj=C()
obj.m1()
obj.m2()
obj.m3()