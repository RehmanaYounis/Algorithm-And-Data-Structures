class Solution:
    def largestVariance(self, s: str) -> int:
        # Create a dictionary with the count of all chars of s
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        # Calculate the possible permulations
        permutations = itertools.permutations(chars, 2)
        
		# Calculate the max subarray count with kadene algo
        count = 0
        for a, b in permutations:
            count = max(self.kadene(a, b, s, chars), count)
        return count

    def kadene(self, a, b, s, chars):
        count = 0
        max_local = 0

		# Keep track if c has become a or b
        is_a = False
        is_b = False

		# Keep track of characters for a and b
        val_a = chars[a]
        val_b = chars[b]
        for c in s:

			# No need to continue if c is not a or b
            if c != a and c != b:
                continue

			# Reset the max_local if there are no chars left or max_total
		    # is negative
            if max_local < 0 and val_a != 0 and val_b != 0:
                max_local = 0
                is_a = False
                is_b = False

			# Add 1 to the local max if c is the expected char
            if c == a:
                max_local += 1
                val_a -= 1
                is_a = True
						
			# Remove 1 from the local max if c is the expected char
            if c == b:
                max_local -= 1
                val_b -=1
                is_b = True
            
			# Only calculate the count if a and b apperared
            if is_a and is_b:
                count = max(count, max_local)
        return count