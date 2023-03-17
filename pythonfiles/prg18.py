class PrimeNum():
    def __init__(self):
        self.c=2
        self.r=1
    def accept(self):
        self.n=int(input('enter n value to check prime number:'))
    def process(self):
        while self.c<=self.n//2 and self.r!=0:
            self.r=self.n%self.c
            self.c=self.c+1
    def output(self):
        if self.r!=0:
            print(str(self.n)+ ' is prime number')
        else:
            print(str(self.n)+ ' is not prime number')
d=PrimeNum()
d.accept()
d.process()
d.output()
        
