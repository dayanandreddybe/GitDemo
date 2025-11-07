from OppsDemo import Calculator



class ChildImpl(Calculator):
    num2=200

    def __init__(self):
        self.num2=200
        Calculator.__init__(self,2,10)



    def getcompletedata(self):
        return self.num2+self.num+self.Summation()
obj=ChildImpl()
print(obj.getcompletedata())