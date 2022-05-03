class Solution:
    def canAttendMeetings(self, intervals:[[int]]) -> bool:

        if not intervals:
            return True

        # max,min
        start = 0
        end = 0
        counter = [0] * (10 ** 6)

        for e in intervals:
            start = e[0]
            print("start is")
            print(start)

            end = e[1]
            print("end is")
            print(end)
            length = e[1] - e[0] + 1
            for i in range(length - 1):
                counter[start + i] = counter[start+i] + 1

        print(counter)

        for e in counter:
            if e > 1:
                return False

        return True


if __name__ == '__main__':
    # a = Solution().canAttendMeetings([[1,5],[8,9]])
    #
    # print("answer is ")
    # print(a)
    l = [[1,4], [2,3], [0,10]]
    l.sort()
    print(l)
