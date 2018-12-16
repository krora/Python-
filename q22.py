#
#
from q21q3 import countBreakpoints as countBreakpoints
from q21q3 import hasDecreasingStrips as hasDecreasingStrips
from q21q3 import reversePerm as reversePerm
from q21q3 import getOptimalReversal as getOptimalReversal


def getOptimalReversals(seq):
    rev = []
    optdecr = 0
    origb = countBreakpoints(seq)
    for i in range(1, len(seq) - 2):
        for j in range(i + 1, len(seq) - 1):
            nxt = reversePerm(seq[:], i, j)

            if origb - countBreakpoints(nxt) > optdecr:
                optdecr = origb - countBreakpoints(nxt)
                rev = [(i,j)]
            elif origb - countBreakpoints(nxt) == optdecr:
                rev.append((i,j))
    return rev, optdecr


def improvedBreakpointReversalSort1(seq):
    while countBreakpoints(seq) > 0:
        if hasDecreasingStrips(seq):
            (i, j) = getOptimalReversal(seq)
            reversePerm(seq, i, j)
        else:
            print "Yoo-hoo!"
            print seq
            return True
    return False


def main22():
    ints = [3, 4, 6, 5, 8, 1, 7, 2]
    
    # Add begin and end markers 0 and n+1
    seq = [0] + ints + [len(ints) + 1]
    print seq, "b(seq) =", countBreakpoints(seq)
    allseq = [seq[:]]
    while allseq:
        seq = allseq.pop()
        revs, decr = getOptimalReversals(seq[:])
        for rev in revs:
            nxt = reversePerm(seq[:], *rev)
            allseq.append(nxt[:])
            print 'nxt=', nxt, 'prev', seq, 'decr=', decr
            if improvedBreakpointReversalSort1(nxt[:]) == True:
                print nxt, decr
                print hasDecreasingStrips(nxt)
                return


if __name__ == '__main__':
    print "PROBLEM 2-2"
    main22()
