from IScoreComponent import IScoreComponent

import nltk
from nltk.corpus import words

class TokenScoreComponent(IScoreComponent):

    def __init__(self):
        nltk.download('words')
        self.english_words = set(words.words())

    def _decompose_username(self, username: str) -> list[str]:
        """Decompose a username into the smallest possible set of valid English words or individual characters."""
        
        # Convert username to lowercase for comparison
        username = username.lower()
        
        # Memoization cache to store results of subproblems
        memo = {}
        
        def helper(sub_username):
            """Helper function to find the minimal decomposition of sub_username."""
            if sub_username in memo:
                return memo[sub_username]
            
            # Base case: if the whole substring is a valid word
            if sub_username in self.english_words:
                return [sub_username]

            min_decomposition = None

            # Try every possible split position
            for i in range(1, len(sub_username) + 1):
                prefix = sub_username[:i]
                if prefix in self.english_words:
                    suffix_decomposition = helper(sub_username[i:])
                    if suffix_decomposition is not None:
                        decomposition = [prefix] + suffix_decomposition
                        if min_decomposition is None or len(decomposition) < len(min_decomposition):
                            min_decomposition = decomposition

            # If no valid word-based decomposition found, split into individual characters
            if min_decomposition is None:
                min_decomposition = []
                i = 0
                while i < len(sub_username):
                    # Find the longest valid word starting from index i
                    for j in range(len(sub_username), i, -1):
                        if sub_username[i:j] in self.english_words:
                            min_decomposition.append(sub_username[i:j])
                            i = j
                            break
                    else:
                        # If no valid word found, add the single character and move forward
                        min_decomposition.append(sub_username[i])
                        i += 1

            memo[sub_username] = min_decomposition
            return min_decomposition
        
        # Call the helper function on the full username
        return helper(username)

    def score_username(self, name):
        decomp = self._decompose_username(name)
        
        # count number of real-word tokens
        total = 0
        real = 0
        s2 = 0
        for word in decomp:
            total += 1
            if len(word) > 1:
                real += 1
                s2 += len(word)
        s1 = total / real
        s2 /= len(name)
        
        return (s1 + s2) / 2
