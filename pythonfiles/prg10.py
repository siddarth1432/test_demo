class Sum:
    def __init__(self):
        self.sum=0
        self.c=1
    def accept(self):
        self.n=int(input('enter n value:'))
    def process(self):
        while self.c<self.n:
            self.r=self.n%self.c
            if self.r==0:
                print(self.c)
                self.sum=self.sum+self.c
            self.c=self.c+1        
    def output(self):
        if self.sum==self.n:
            print('PERFECT NUMBER')
        else:
            print('NOT PERFECT NUMBER')
        
d=Sum()
d.accept()
d.process()
d.output()
