class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]
        subset=[]
        def backTrack(i, total):
            if i >=len(candidates) or total>target:
                return
            if total == target:
                print(subset)
                output.append(subset.copy())
                return
            subset.append(candidates[i])
            backTrack(i, total+candidates[i])
            
            subset.pop()
            backTrack(i+1, total)
            
        backTrack(0, 0)
        return output
    