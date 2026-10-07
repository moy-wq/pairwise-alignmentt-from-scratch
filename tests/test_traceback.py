from pairwise_alignment.algorithms.needleman_wunsch.algorithm.matrix import AlignmentMatrix
from pairwise_alignment.core.scoring import ScoringScheme
from pairwise_alignment.algorithms.needleman_wunsch.algorithm.traceback import Traceback


def test_traceback_identical_sequences():
    seqA = "A"
    seqB = "A"

    scoring = ScoringScheme(
        match=1,
        mismatch=-1,
        gap=-2
    )

    matrix = AlignmentMatrix(seqA, seqB)
    matrix.initialize_matrix(scoring.gap)
    matrix.fill_matrix(scoring)

    traceback = Traceback(
        matrix.matrix,
        seqA,
        seqB,
        scoring
    )

    assert traceback.run() == ["D"]



    