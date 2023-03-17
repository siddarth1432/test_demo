class DisplaySumOdd:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.i=int(input('enter initial value:'))
        self.f=int(input('enter final vakue:'))
    def process(self):
        while self.i<=self.f:
            self.r=self.i%2
            if self.r!=0:
                print(self.i,end='  ')
                self.sum=self.sum+self.i
            self.i=self.i+1
    def output(self):
        print('\n sum:',self.sum)
d=DisplaySumOdd()
d.accept()
d.process()
d.output()
    
