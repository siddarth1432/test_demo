class Sum:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input('enter n value:'))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.sum=self.r+self.sum
            self.n=self.n//10
    def output(self):
        print('sum of digits:',self.sum)
d=Sum()
d.accept()
d.process()
d.output()

