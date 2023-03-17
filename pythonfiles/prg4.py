class DisplayNNumbers:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input('enter number:'))
    def process(self):
        while self.c<=self.n:
            print(self.c)
            self.c=self.c+1
d=DisplayNNumbers()
d.accept()
d.process()
