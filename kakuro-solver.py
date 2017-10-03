import numpy as np

class  KakuroLineRow:
    def __init__(self, sum, fields):
        #"target sum" for this linerow
        self.sum = sum
        #list of integer corresponding to the kakuro grid fields of this linerow
        self.fields = fields



class Kakuro:
    def __init__(self, linSize):
        self.linSize = linSize
        self.size = linSize*linSize
        #list holding the actual number values of the kakuro,
        # "-1" indicates value not set:
        self.grid = [-1]*self.size
        # list holding KakuroLineRow's describing the kakuro:
        self.linerows = list()

    def checkLinerow(self,linerow):
        # get number values of linerow (only fields which are set and not anchors)
        values = [self.grid[f] for f in linerow.fields if self.grid[f] > 0]
        # if all fields of linerow are set and the sum does not match
        # the target sum, the kakuro is not solvable
        if len(values) == len(linerow.fields):
            if sum(values) != linerow.sum:
                return False

        # kakuro is not solvable if partial sum already exceeds target sum:
        if sum(values)>linerow.sum:
            return False

        # kakuro is not solvable if there are duplicate values:
        if len(values) != len(set(values)):
            return False
        return True

    def isSolvable(self):
        #a kakuro is solvable if each linerow is valid
        for lr in self.linerows:
            if not self.checkLinerow(lr):
                return False
        return True

    def isSolved(self):
        #a kakuro is not solved if it is not solvable
        if not kakuro.isSolvable():
            return False
        #if not all fields referenced in all linerows are set,
        #the kakuro is not solved:
        for lr in self.linerows:
            for f in lr.fields:
                if self.grid[f] == -1:
                    return False
        #if the target sums are not met, the kakuro is not solved:
        for lr in self.linerows:
            if sum([self.grid[f] for f in lr.fields]) != lr.sum:
                return False
        #else it is solved:
        return True



    def addLineRow(self,linerow):
        self.linerows.append(linerow)

    def addAnchor(self,field):
        self.grid[field] = -2

    def display(self):
        for i in range(0,self.linSize):
            for j in range(0,self.linSize):
                if self.grid[self.linSize*i+j] > 0:
                    print(self.grid[self.linSize*i+j],end=" ")
                if self.grid[self.linSize*i+j] == -2:
                    print("x", end=" ")
                if self.grid[self.linSize*i+j] == -1:
                    print(".", end=" ")

            print("")
        print("")



import random

def recursiveSolveKakuro(kakuro):
    if random.random()<1:
        kakuro.display()
    if kakuro.isSolved():
        return kakuro
    else:
        for i in range(0,kakuro.size):
            if kakuro.grid[i] == -1: #unset field
                for n in range(1,10):
                    if(kakuro.isSolvable()):
                        kakuro.grid[i] = n
                        try_kakuro = recursiveSolveKakuro(kakuro)
                        if(try_kakuro != None):
                            return try_kakuro
                        else:
                            kakuro.grid[i] = -1
                return None





if __name__ == '__main__':
    n=6
    kakuro = Kakuro(6)

    #lines
    kakuro.addLineRow(KakuroLineRow(8,(0,1)))
    kakuro.addLineRow(KakuroLineRow(17,(6,7,8)))
    kakuro.addLineRow(KakuroLineRow(11,(14,15,16)))
    kakuro.addLineRow(KakuroLineRow(23,(19,20,21,22)))
    kakuro.addLineRow(KakuroLineRow(9,(24,25,26)))
    kakuro.addLineRow(KakuroLineRow(14,(30,31)))
    kakuro.addLineRow(KakuroLineRow(8,(4,5)))
    kakuro.addLineRow(KakuroLineRow(7,(10,11)))
    kakuro.addLineRow(KakuroLineRow(16,(28,29)))
    kakuro.addLineRow(KakuroLineRow(8,(34,35)))
    #row
    kakuro.addLineRow(KakuroLineRow(11,(0,6)))
    kakuro.addLineRow(KakuroLineRow(13,(1,7)))
    kakuro.addLineRow(KakuroLineRow(26,(4,10,16,22,28,34)))
    kakuro.addLineRow(KakuroLineRow(10,(5,11)))
    kakuro.addLineRow(KakuroLineRow(11,(8,14,20,26)))
    kakuro.addLineRow(KakuroLineRow(14,(15,21)))
    kakuro.addLineRow(KakuroLineRow(15,(19,25,31)))
    kakuro.addLineRow(KakuroLineRow(12,(24,30)))
    kakuro.addLineRow(KakuroLineRow(9,(29,35)))

    # anchor fields
    kakuro.addAnchor(2)
    kakuro.addAnchor(3)
    kakuro.addAnchor(9)
    kakuro.addAnchor(12)
    kakuro.addAnchor(13)
    kakuro.addAnchor(17)
    kakuro.addAnchor(18)
    kakuro.addAnchor(23)
    kakuro.addAnchor(27)
    kakuro.addAnchor(32)
    kakuro.addAnchor(33)
    kakuro.display()

    kakuro.isSolvable()
    kakuro.linerows[0].fields
    sk=recursiveSolveKakuro(kakuro)
    sk.display()
    sk.isSolved()
