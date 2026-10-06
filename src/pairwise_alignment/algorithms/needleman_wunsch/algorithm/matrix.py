import numpy as np
import pairwise_alignment.core.scoring as scoring


class AlignmentMatrix:
    def __init__(self, seqA: str, seqB: str):
        self.seqA = seqA
        self.seqB = seqB

        self.matrix = np.full((len(seqA) + 1, len(seqB)+ 1) , None, dtype=object)


    def initialize_matrix(self, gap_penalty:int)-> None:
        self.matrix[0,0] = 0
        for j in range(len(self.seqB) + 1):
            self.matrix[0, j] = j * gap_penalty

        for i in range(len(self.seqA) + 1):
            self.matrix[i, 0] = i * gap_penalty

    def fill_matrix(self, scoring_method: scoring.ScoringScheme) -> None:
        lines = self.matrix.shape[0]
        columns = self.matrix.shape[1]
        
        for i in range(1,lines):
            for j in range(1,columns):
                self.matrix[i,j] = max(self.matrix[i - 1, j - 1] + scoring_method.score(self.seqA[i - 1],
                                    self.seqB[j - 1]),
                                    self.matrix[i-1,j] + scoring_method.gap,
                                    self.matrix[i,j-1] + scoring_method.gap)