class AlignedSequence:
    def __init__(self, aligned_A, aligned_B, score: ScoringScheme):
        self.aligned_A = aligned_A
        self.aligned_B = aligned_B
        self.score = score
