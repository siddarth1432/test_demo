class ReadNum():
    def __init__(self):
        pass
    def accept(self):
        self.a=int(input("enter A value:"))
        self.b=int(input("enter B value:"))
    def process(self):
        while self.a!=self.b:
            if self.a>self.b:
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
    def output(self):
        print(self.a)
d=ReadNum()
d.accept()
d.process()
d.output()
    
