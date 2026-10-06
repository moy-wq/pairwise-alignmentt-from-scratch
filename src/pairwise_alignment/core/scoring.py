class ScoringScheme:
    def __init__(self, match, mismatch, gap):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap


    def score(self, A: str, B: str) -> int:
        if A == '-' or B == '-':
            return self.gap
        
        return self.match if A == B else self.mismatch

    
    