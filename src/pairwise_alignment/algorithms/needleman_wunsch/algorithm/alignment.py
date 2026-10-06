class Alignment:
    def __init__(self, seqA, seqB, moves):
        self.seqA = seqA
        self.seqB = seqB
        self.moves = moves

    def build(self):
        aligned_A = []
        aligned_B = []
        i = 0
        j = 0

        for move in self.moves:
            if move == "D":
                aligned_A.append(self.seqA[i])
                aligned_B.append(self.seqB[j])
                i += 1
                j += 1

            elif move == "E":
                aligned_A.append("-")
                aligned_B.append(self.seqB[j])
                j += 1

            elif move == "C":
                aligned_A.append(self.seqA[i])
                aligned_B.append("-")
                i += 1

        return "".join(aligned_A), "".join(aligned_B)


    