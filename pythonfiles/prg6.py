class DisplayOddNum:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input('enter number:'))
    def process(self):
        while self.c<=self.n:
            self.r=self.c%2
            if self.r!=0:
                print(self.c)
            self.c=self.c+1
d=DisplayOddNum()
d.accept()
d.process()
