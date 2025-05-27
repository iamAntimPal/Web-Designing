from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]
   
solution = Solution()
words = ["leet","code"]
x = input("Enter a character: ")
result = solution.findWordsContaining(words, x)
print(result)