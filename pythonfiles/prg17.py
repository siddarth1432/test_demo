#program to display mathematical table
class TableText:
    def __init__(self):
        self.i=1
    def accept(self):
        self.n=int(input("enter number to display table:"))
    def process(self):
        while self.i<11:
            print('{} * {}={}'.format(self.n,self.i,self.n*self.i))
d=TableText()
d.accept()
d.process()
            
        
        
