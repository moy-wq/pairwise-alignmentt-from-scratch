import numpy as np

from pairwise_alignment.algorithms.needleman_wunsch.algorithm.matrix import AlignmentMatrix
from pairwise_alignment.core.scoring import ScoringScheme

def test_matrix():
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

    expected = np.array([
        [0, -2],
        [-2, 1]
    ], dtype=object)

    assert np.array_equal(matrix.matrix, expected)

def test_fill_matrix():
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

    expected = np.array([
        [0, -2],
        [-2, 1]
    ], dtype=object)

    assert np.array_equal(matrix.matrix, expected)





if __name__ == "__main__":
    test_matrix()
    print("Teste passou!")
