#
#
import itertools


def countBreakpoints(seq):
    answer = 0
    for i in range(len(seq) - 1):
        if seq[i] != seq[i + 1] + 1 and seq[i] != seq[i + 1] - 1:
            answer += 1
    return answer


def hasDecreasingStrips(seq):
    for i in range(1, len(seq) - 1):
        if seq[i - 1] + 1 != seq[i] and seq[i] + 1 != seq[i + 1]:
            return True
    return False


def reversePerm(seq, i, j):
    for lft in range((j - i + 1) / 2):
        rgt = j - i - lft
        seq[i + lft], seq[i + rgt] = seq[i + rgt], seq[i + lft]
    return seq


def getOptimalReversal(seq):
    origb = countBreakpoints(seq)
    optdecr = 0
    optrev = (0, 0)
    for i in range(1, len(seq) - 2):
        for j in range(i + 1, len(seq) - 1):
            rgt = seq[i] - seq[j + 1]
            lft = seq[i - 1] - seq[j]
            if lft in (1, -1) or rgt in (1, -1):
                nxt = reversePerm(seq[:], i, j)
                if origb - countBreakpoints(nxt) > optdecr:
                    optdecr = origb - countBreakpoints(nxt)
                    optrev = (i, j)

                if optdecr == 2: return optrev
    return optrev


def getFlipReversal(seq):
    if not hasDecreasingStrips(seq):
        return (0, 0)
    i = 1
    while i < len(seq) - 1 and seq[i] + 1 != seq[i + 1]:
        i += 1
    j = i + 1
    while j < len(seq) - 2 and seq[j] + 1 == seq[j + 1]:
        j += 1
    return (i, j)


def improvedBreakpointReversalSort(seq):
    step = 0
    while countBreakpoints(seq) > 0:
        step += 1
        print "step =", step
        orig = seq[:]
        if hasDecreasingStrips(seq):
            (i, j) = getOptimalReversal(seq)
            reversePerm(seq, i, j)
        else:
            (i, j) = getFlipReversal(seq)
            reversePerm(seq, i, j)
        print orig, "rev_i, rev_j =", i, j
        print seq, "b(seq) =", countBreakpoints(seq)
    return seq


def getReversal(seq):
    ndall = []
    length = len(seq)
    for nxt in list(itertools.permutations(seq[1:-1], length - 2)):
        nxt = [0] + list(nxt) + [length - 1]
        if not hasDecreasingStrips(nxt):
            ndall.append(nxt)
    for seq in ndall:
        print "no decr,", seq, hasDecreasingStrips(seq)
    for seq in ndall:
        for i in range(1, len(seq)-2):
            for j in range(i + 1, len(seq)-1):
                rgt = seq[i] - seq[j + 1]
                lft = seq[i - 1] - seq[j]
                if lft in (1, -1) or rgt in (1, -1):
                    nxt = reversePerm(seq[:], i, j)
                    if countBreakpoints(seq) > countBreakpoints(nxt):
                        print seq, "b(nd) =", countBreakpoints(seq)
                        print nxt, "b(nxt) =", countBreakpoints(nxt)
                        print "rev_i, rev_j =", i, j
                        return nxt


def main21():
    seq = [0, 3, 4, 6, 5, 8, 1, 7, 2, 9]
    improvedBreakpointReversalSort(seq)


def main3():
    seq = [0, 1, 2, 3, 4, 5, 6]
    seq = getReversal(seq)
    improvedBreakpointReversalSort(seq)


if __name__ == '__main__':
    print "PROBLEM 2-1"
    main21()
    print "PROBLEM 3"
    main3()
