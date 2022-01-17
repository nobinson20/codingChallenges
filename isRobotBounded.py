class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dup_ins = instructions*4
        a, b = 0
        pos = (a, b)
        cnt = (0, 1)

        for e in dup_ins:
            if e == 'G':
                pos = pos + cnt



