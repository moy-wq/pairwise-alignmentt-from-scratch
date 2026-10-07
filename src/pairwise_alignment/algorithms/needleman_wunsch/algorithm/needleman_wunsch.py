from pairwise_alignment.algorithms.needleman_wunsch.algorithm.matrix import AlignmentMatrix 
from pairwise_alignment.core.alignment import Alignment
from pairwise_alignment.core.result import AlignedSequence
from pairwise_alignment.algorithms.needleman_wunsch.algorithm.traceback import Traceback



class NeedlemanWunsch:

    def __init__(self, seqA, seqB, scoring_method):
        self.seqA = seqA
        self.seqB = seqB
        self.scoring = scoring_method


    def run(self):
        matrix = AlignmentMatrix(
            self.seqA,
            self.seqB
        )

        matrix.initialize_matrix(self.scoring.gap)
        matrix.fill_matrix(self.scoring)

        traceback = Traceback(
            matrix.matrix,
            self.seqA,
            self.seqB,
            self.scoring
        )

        moves = traceback.run()

        alignment = Alignment(
            self.seqA,
            self.seqB,
            moves
        )

        aligned_A, aligned_B = alignment.build()

        result = AlignedSequence(aligned_A=aligned_A, aligned_B=aligned_B, score=matrix.matrix[-1,-1])

        return result

    
