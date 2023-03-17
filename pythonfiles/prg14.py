class Demo:
    def __init__(self):
        self.result=1
        self.c=1
    def accept(self):
        self.b=int(input("enter b value:"))
        self.p=int(input("enter p value:"))
    def process(self):
        while self.c<=self.p:
            self.result=self.result*self.b
            self.c=self.c+1
    def output(self):
        print("{} to the power {} ={}:".format(self.b,self.p,self.result))
d=Demo()
d.accept()
d.process()
d.output()
