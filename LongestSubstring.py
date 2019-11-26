class Solution():

    @classmethod
    def longestSubstring(self, s):
        '''
        :param s: string
        :return: integer
        '''

        dicts ={}
        maxLength = start = 0

        for i, c in enumerate (s):
            if c in dicts and dicts[c] >= start:
                start = dicts [c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            dicts[c] = i
        return maxLength

s = 'abeccfe'
def main():
    x = Solution.longestSubstring(s)
    print('The longest substring without repeating is {}'.
          format(x))

if __name__ == '__main__':
    main()