from needleman_wunsch.algorithm.matrix import AlignmentMatrix
from needleman_wunsch.algorithm.scoring import ScoringScheme
from needleman_wunsch.algorithm.traceback import Traceback


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



    