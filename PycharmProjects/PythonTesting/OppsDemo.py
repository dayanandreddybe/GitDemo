class Calculator:
    num =100
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Print i am called automatically ")
    def getData(self):
        print("I am now executing as a method in class")
    def Summation(self):
        return self.a+self.b+Calculator.num

a=Calculator(2,3)
print(a.num)
print(a.getData())
print(a.Summation())
b=Calculator(5,4)
print(b.num)
print(b.getData())
print(b.Summation())