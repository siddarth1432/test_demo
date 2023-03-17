class Armstrong:
    def __init__(self):
        self.sum=0
        self.c=0
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        num=self.n
        while num>0:
            self.r=num%10
            self.sum=self.sum+self.r**3
            num=num//10
        self.c=self.c+1
    def output(self):
        
        if self.n==self.sum:
            print('AN ARMSTRONG NUMBER')
        else:
            print('NOT AN ARMSTRONG NUMBER')
d=Armstrong()
d.accept()
d.process()
d.output()
