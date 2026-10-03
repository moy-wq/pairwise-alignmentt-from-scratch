import numpy as np


class AlignmentMatrix:
    def __init__(self, seqA: str, seqB: str):
        self.seqA = seqA
        self.seqB = seqB

        self.matrix = np.array([[p for p in seqA], [p for p in seqB]])



        