import unittest
class Board:
    def __init__(self,matrix=[]):
        self.matrix = matrix

    def zeros(self,N):
        self.matrix=[]
        for i in range(N):
            self.matrix.append([])
            for j in range(N):
                self.matrix[i].append(0)

    def putOnes(self,positions):
        N = len(self.matrix)
        for pos in positions:
            row = pos/N
            col = pos%N
            self.matrix[row][col]=1

    def setFromList(self,seq,N):
        self.matrix = []
        for i in range(N):
            self.matrix.append([])

        for row in range(N):
            for col in range(N):
                self.matrix[row].append(seq[row*N+col])

    def getList(self):
        seq = []
        N=len(self.matrix)
        for row in range(N):
            for col in range(N):
                seq.append(self.matrix[row][col])
        return seq

    def show(self):
        for row in self.matrix:
            print row
    def nqueens(self):
        queens = 0
        for row in self.matrix:
            for item in row:
                queens+=item
        return queens

    def reviewHorizontals(self):
        attacks = 0
        for row in self.matrix:
            queens = 0
            for item in row:
                if item==1: 
                    queens+=1
            if queens>0:
                attacks+=queens-1
        return attacks

    def reviewVerticals(self):
        if len(self.matrix)==0:
            return 0
        attacks=0
        for col in range(len(self.matrix[0])):
            queens=0
            for row in range(len(self.matrix)):
                if self.matrix[row][col]==1:
                    queens+=1
            if queens>0:
                attacks+=queens-1
        return attacks

    def reviewDiagonals(self):
        heads = []
        heads2 = []
        for i in range(len(self.matrix)):
            heads.append([0,i])
            heads2.append([0,i])
            if i>0:
                heads.append([i,len(self.matrix)-1])
                heads2.append([i,0])
        attacks = 0
        for head in heads:
            row = head[0]
            col = head[1]
            queens = 0
            while row<=(len(self.matrix)-1) and col>=0:
                if self.matrix[row][col]==1:
                    queens+=1
                row+=1
                col-=1
            if queens>0:
                attacks+=queens-1
        for head in heads2:
            row = head[0]
            col = head[1]
            queens=0
            while row<=(len(self.matrix)-1) and col<=(len(self.matrix)-1):
                if self.matrix[row][col]==1:
                    queens+=1
                row+=1
                col+=1
            if queens>0:
                attacks+=queens-1
        return attacks

class TestBoard(unittest.TestCase):
    
    def testZeros(self):
        boardMat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        b = Board()
        b.zeros(4)
        self.assertEqual(b.matrix,boardMat)

    def testZeros(self):
        boardMat = [[0,0,1,0],[1,0,0,0],[0,0,0,1],[1,0,1,0]]
        b = Board()
        b.zeros(4)
        ones = [2,4,11,12,14]
        b.putOnes(ones)
        self.assertEqual(b.matrix,boardMat)

    def testBoardToList(self):
        boardMat = [[0,1,0,0],[0,0,0,0],[0,0,1,0],[1,0,0,0]]
        boardVec = [0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0]
        b = Board(boardMat)
        self.assertEqual(boardVec,b.getList())

    def testBoardFromList(self):
        boardMat = [[0,1,0,0],[0,0,0,0],[0,0,1,0],[1,0,0,0]]
        boardVec = [0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0]
        b = Board()
        b.setFromList(boardVec,4)
        self.assertEqual(boardMat,b.matrix)

    def testHorizontalReview(self):
        boardMat = [[0,1,0,0],[0,0,1,1],[1,0,1,1],[0,1,0,0]]
        b = Board(boardMat)
        self.assertEqual(b.reviewHorizontals(),3) 

    def testVerticalReview(self):
        boardMat = [[0,1,0,1],[0,0,1,1],[1,0,1,1],[0,1,0,0]]
        b = Board(boardMat)
        self.assertEqual(b.reviewVerticals(),4)        

    def testDiagonalsReview(self):
        boardMat = [[0,1,0,1],[0,0,1,1],[1,0,1,1],[0,1,0,0]]
        b = Board(boardMat)
        self.assertEqual(b.reviewDiagonals(),6)        

if __name__ == '__main__':
    unittest.main()