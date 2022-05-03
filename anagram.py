class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = sorted(list(s))
        tl = sorted(list(t))

        slen = len(sl)
        tlen = len(tl)

        if slen != tlen:
            return False

        for i in range(slen):
            if sl[i] != tl[i]:
                return False

        return True



if __name__ == '__main__':


