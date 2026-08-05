class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        var = {
            "2":"abc",
            "3":"def", 
            "4":"ghi",
            "5":"jkl", 
            "6":"mno", 
            "7":"pqrs", 
            "8":"tuv", 
            "9":"wxyz"
            }

        def dfs(i, combo):
            if len(combo) == len(digits):
                res.append(combo)
                return
            for char in var[digits[i]]:
                dfs(i + 1, combo + char)
        
        if digits:
            dfs(0, "")
        return res