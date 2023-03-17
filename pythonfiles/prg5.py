class DisplayNumbers:
    def accept(self):
        self.i=int(input('enter inintial number:'))
        self.f=int(input('enter final value:'))
    def process(self):
        while self.f>=self.i:
            print(self.f,end='  ')
            self.f=self.f-1
d=DisplayNumbers()
d.accept()
d.process()
