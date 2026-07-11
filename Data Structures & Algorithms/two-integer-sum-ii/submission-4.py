class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        p1 = 0
        p2 = n-1


        """while p2 < n and numbers[p2] < target:
            p2 += 1"""

        a = numbers[p1]
        b = numbers[p2]

        print()

        

        while a+b != target: #and p1<p2 and p2<n:
            print(a, b)
            if numbers[p1+1] + b > target:
                p2 -= 1
                b = numbers[p2]

            else:
                p1 += 1
                a = numbers[p1]



            """print(a, b)
            if p2 < n-1 or a + numbers[p2+1] > target:
                p1 += 1
                a = numbers[p1]
            else:
                p2 += 1
                b = numbers[p2]"""

        return [p1+1, p2+1]
        