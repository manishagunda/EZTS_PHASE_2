class A:
    def m1(self):
        print("method m1 in class A")
class B(A):
    def m2(self):
        print("method m2 in class B")
class C(B):
    def m3(self):
        print("method m3 in class B")
obj=C()
obj.m1()
obj.m2()
obj.m3()