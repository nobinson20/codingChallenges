class Solution:
    def isPalindrome(self, s: str) -> bool:
        # to lowercase
        s = s.lower()

        # remove non-alphanumeric characters (incl. blanks)
        s = ''.join(ch for ch in s if ch.isalnum())

        for i in range(0, len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True


if __name__ == '__main__':
    output = Solution.isPalindrome(Solution, "123")

    print(output)