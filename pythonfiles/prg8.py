class Demo:
    def accept(self):
        self.n=int(input('enter a num divisble by 2 and 5:'))
    def process(self):
        if self.n%2==0 and self.n%5==0:
            print('divisible')
        else:
            print('not divisible')
d=Demo()
d.accept()
d.process()
