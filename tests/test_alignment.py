from needleman_wunsch.algorithm.alignment import Alignment


def test_build_alignment():
    seqA = "GAC"
    seqB = "GC"

    moves = ["D", "C", "D"]

    alignment = Alignment(seqA, seqB, moves)

    aligned_A, aligned_B = alignment.build()

    assert aligned_A == "GAC"
    assert aligned_B == "G-C"