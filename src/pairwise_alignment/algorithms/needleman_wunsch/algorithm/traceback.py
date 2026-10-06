class Traceback:

    def __init__(self, matrix, seqA, seqB, scoring_method):
        self.matrix = matrix
        self.seqA = seqA
        self.seqB = seqB
        self.scoring_method = scoring_method

    def run(self):
        i = len(self.seqA)
        j = len(self.seqB)
        result = []
        while i > 0 or j >0:
            element = self.matrix[i,j]

            if i == 0:
                result.append("E")
                j -=1
            elif j ==0:
                result.append("C")
                i-=1
            else: 

                if self.matrix[i - 1, j - 1] + self.scoring_method.score(self.seqA[i-1], self.seqB[j-1]) == element:
                    result.append("D")
                    i-= 1
                    j-=1
                elif self.matrix[i, j - 1] + self.scoring_method.gap == element:
                    result.append("E")
                    j -= 1
                elif self.matrix[i-1, j] + self.scoring_method.gap == element:
                    result.append("C")
                    i -= 1

        result.reverse()
        return result
