import numpy as np

class KakuroLineRow:
    def __init__(self, ksum, fields):
        self.ksum = ksum
        self.fields = fields
    ksum = 0
    fields = list()

def isValid(klr):
    values = []
    klr=kakuro[0]
    for f in klr.fields:
        values.append(grid[f])
    #find duplicates
    for v in values:
        if v==0:
            continue
        if values.count(v)>1:
            return False

    if sum(values)>klr.ksum:
        return False

    return True
n=6
grid = np.zeros(n*n)

kakuro = []
#lines
kakuro.append(KakuroLineRow(8,(0,1)))
kakuro.append(KakuroLineRow(17,(6,7,8)))
kakuro.append(KakuroLineRow(11,(14,15,16)))
kakuro.append(KakuroLineRow(23,(17,18,19,20)))
kakuro.append(KakuroLineRow(9,(24,25,26)))
kakuro.append(KakuroLineRow(14,(30,31)))
kakuro.append(KakuroLineRow(8,(4,5)))
kakuro.append(KakuroLineRow(8,(10,11)))
kakuro.append(KakuroLineRow(16,(28,29)))
kakuro.append(KakuroLineRow(8,(34,35)))
#row
kakuro.append(KakuroLineRow(11,(0,6)))
kakuro.append(KakuroLineRow(13,(1,7)))
kakuro.append(KakuroLineRow(26,(4,10)))
kakuro.append(KakuroLineRow(10,(5,11)))
kakuro.append(KakuroLineRow(11,(8,14,20,26)))
kakuro.append(KakuroLineRow(14,(15,21)))
kakuro.append(KakuroLineRow(15,(19,20,21)))
kakuro.append(KakuroLineRow(12,(24,30)))
kakuro.append(KakuroLineRow(9,(25,31)))


isValid(kakuro[0])

solved=False

while(not solved):
    
