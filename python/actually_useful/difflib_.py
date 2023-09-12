from difflib import SequenceMatcher

s = SequenceMatcher(None, "salt", "salutations")
print(s.ratio())
