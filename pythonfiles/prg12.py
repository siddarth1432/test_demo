class SumofSquares:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter a number:"))
    def process(self):
        while self.n>0:
            r=self.n%2
            self.sum=self.sum+r**2
            self.n=self.n//10
    def output(self):
        print("the sum of the squares of digits of the number:",self.sum)
d=SumofSquares()
d.accept()
d.process()
d.output()
