class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        m_odd=math.ceil(m/2)
        m_even=m//2
        n_odd=math.ceil(n/2)
        n_even=n//2
        return (m_odd*n_even)+(n_odd*m_even)