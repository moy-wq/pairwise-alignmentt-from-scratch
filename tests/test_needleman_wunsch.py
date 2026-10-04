from needleman_wunsch.algorithm.needleman_wunsch import NeedlemanWunsch
from needleman_wunsch.algorithm.scoring import ScoringScheme

def test_needleman_wunsch():
    seqA = "GAC"
    seqB = "GC"

    scoring = ScoringScheme(
        match=1,
        mismatch=-1,
        gap=-2
    )

    nw = NeedlemanWunsch(
        seqA,
        seqB,
        scoring
    )

    result = nw.run()

    assert result.aligned_A == "GAC"
    assert result.aligned_B == "G-C"
    assert result.score == 0