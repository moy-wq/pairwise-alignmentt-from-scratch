from pairwise_alignment.algorithms.smith_waterman.algorithm.matrix import SmithWatermanMatrix
from pairwise_alignment.core.alignment import Alignment
from pairwise_alignment.core.scoring import ScoringScheme
from pairwise_alignment.algorithms.smith_waterman.algorithm.traceback import SmithWatermanTraceback
from pairwise_alignment.core.result import AlignedSequence

import numpy as np

class SmithWaterman:

    def __init__(self, seqA, seqB, scoring_method):
        self.seqA = seqA
        self.seqB = seqB
        self.scoring = scoring_method


    def run(self):
        matrix = SmithWatermanMatrix(
            self.seqA,
            self.seqB
        )

        matrix.initialize_matrix(self.scoring.gap)
        matrix.fill_matrix(self.scoring)
        
        traceback = SmithWatermanTraceback(
            matrix.matrix,
            self.seqA, 
            self.seqB,
            self.scoring
        )
        moves = traceback.run()

        alignment = Alignment(  self.seqA,
                                self.seqB,
                                moves=moves)

        alignmentA, alignmentB = alignment.build()

        i, j = np.unravel_index(
            np.argmax(matrix.matrix),
            matrix.matrix.shape
        )

        return AlignedSequence(
            aligned_A=alignmentA,
            aligned_B=alignmentB,
            score=matrix.matrix[i,j])
        



        