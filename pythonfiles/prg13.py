class NumofDig:
    def __init__(self):
        self.c=0
        self.sum=0
    def accept(self):
        self.n=int(input("enter the number:"))
    def process(self):
        while self.n>0:
            self.c=self.c+1
            self.n=self.n//10
    def output(self):
        print("number of digits of {} is {}:".format(self.n,self.c))
d=NumofDig()
d.accept()
d.process()
d.output()
