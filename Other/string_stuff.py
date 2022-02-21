"""
prints OK if palindrome
"""

word = input("Enter A Word: ")
word = word.replace(' ', '').lower()
first = word[: len(word) // 2]
second = word[-1: len(word) // 2: -1]
if first == second:
    print("OK")
else:
    print("NOT OK")
