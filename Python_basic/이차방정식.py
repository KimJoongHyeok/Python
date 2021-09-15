import math

class QE:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getDiscriminant(self):
        return self.b * self.b - 4 * self.a * self.c
    def getRoot(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.b + self.getDiscriminant())/(2*self.a)
    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            return (-self.b + self.getDiscriminant())/(2*self.a)
