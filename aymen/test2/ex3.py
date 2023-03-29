class Solution:
  def __init__(self):
        self.ways = 0
  def climbStairs(self, n: int) -> int:
      map = {1:1,2:2}
      for i in range(3,n+1):
          map[i] = map[i-1] + map[i-2]
      return map[n]
s = Solution()
print(s.climbStairs(35))
