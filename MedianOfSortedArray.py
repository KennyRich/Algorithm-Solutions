A = [1, 2, 3, 4, 5, 6]
B = [1, 3, 5, 7, 9, 11]


class Solution(object):
    @classmethod
    def findMedianSortedArrays(self, A, B):

        '''
        :param A: List[int]
        :param B: List[int]
        :return: float
        '''

        def get_kth_smallest(a_start, b_start, k):

            if k <= 0 or k > len(A) - a_start + len(B) - b_start:
                raise ValueError('k is out of bounds of the input list')

            if a_start >= len(A):
                return B[b_start + k - 1]
            if b_start >= len(B):
                return A[a_start + k - 1]
            if k == 1:
                return min(A[a_start], B[b_start])

            mid_A, mid_B = float('inf'), float('inf')
            if k // 2 - 1 < len(A) - a_start:
                mid_A = A[a_start + k // 2 - 1]
            if k // 2 - 1 < len(B) - b_start:
                mid_B = B[b_start + k // 2 - 1]

            if mid_A < mid_B:
                return get_kth_smallest(a_start + k // 2, b_start, k - k // 2)
            return get_kth_smallest(a_start, b_start + k // 2, k - k // 2)

        right = get_kth_smallest(0, 0, 1 + (len(A) + len(B)) // 2)
        if (len(A) + len(B)) % 2 == 1:
            return right

        left = get_kth_smallest(0, 0, (len(A) + len(B)) // 2)
        return (left + right) / 2.0


def main():
    result = Solution.findMedianSortedArrays(A, B)
    print(result)


if __name__ == '__main__':
    main()
