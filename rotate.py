class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        b=b%len(a)
        for i in xrange(len(a)):
            offset=i+b
            if offset>=len(a):
                offset=offset-len(a)
            ret.append(a[offset])
        return ret
