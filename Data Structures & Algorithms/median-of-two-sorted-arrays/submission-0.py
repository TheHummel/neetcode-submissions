class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1[:]
        B = nums2[:]

        n = len(A)
        m = len(B)

        total = n+m
        half = total //2

        if m < n:
            A, B = B, A
            m, n = n, m

        l = 0
        r = n - 1

        while True:
            i = (r-l) // 2 + l
            j = half - i - 2

            Aleft = A[i] if i>= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < n else float("infinity")
            Bleft = B[j] if j>= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < m else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Bright, Aright)) / 2
            elif Aleft > Bright:
                r = i-1
            else:
                l = i + 1