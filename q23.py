#
#
from q21q3 import countBreakpoints as countBreakpoints
from q21q3 import reversePerm as reversePerm


def getReversals(seq):
    revs = []
    for i in range(1, len(seq) - 2):
        for j in range(i + 1 , len(seq) - 1):
            revs.append(reversePerm(seq[:], i, j))
    return revs


def find5BetterSolutions(seq, maxsteps=4):
    seqall = [(seq[:], [seq[:]], 0)]
    solutions = []

    while seqall:
        seq, hist, step = seqall.pop()

        if countBreakpoints(seq) == 0:
            solutions += [(seq, hist, step)]

        if step >= maxsteps: # permutation is not identity after 4 reversals
            continue

        for rev in getReversals(seq):
            hist_ = hist[:] + [rev[:]]
            seqall.append((rev, hist_, step + 1))

    return sorted(solutions, key=lambda x:x[2])[0:5]


def main23():
    seq = [0, 3, 4, 6, 5, 8, 1, 7, 2, 9]
    seq2 = [0, 1, 3, 2, 5, 4, 6, 7, 8, 9]

    print seq, "b(seq) =", countBreakpoints(seq)
    print find5BetterSolutions(seq)

    print seq2, "b(seq2) =", countBreakpoints(seq2)
    print find5BetterSolutions(seq2)[0][1]


if __name__ == '__main__':
    print "PROBLEM 2-3"
    main23()
