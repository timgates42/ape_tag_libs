from timeit import Timer

def test(testname = 'getfields', numtimes = 1):
    t = Timer('walktree(test, False)', 'from walktree import walktree\nfrom %s import test' % testname)
    print '%s to run %s %i times' % (t.timeit(numtimes), testname, numtimes)

if __name__ == '__main__':
    test()
