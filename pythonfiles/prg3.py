class DisplayNTimes:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input('enter the number:'))
    def process(self):
        while self.c<=self.n:
            print('vanemataram',self.c)
            self.c=self.c+1
d=DisplayNTimes()
d.accept()
d.process()
