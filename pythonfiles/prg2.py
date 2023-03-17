class Display:
    def __init__(self):
        self.i=1
    def process(self):
        while self.i<=10:
            print('vandemataram #',self.i)
            self.i=self.i+1
d=Display()
d.process()
