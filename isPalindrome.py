import re
def is_palindrome(word):
    if word == word[::-1]:
        print(f"The word {word} is Palindrome")
    else:
        print(f"The word {word} is not Palindrome")

word = input("Inter a word to check if it is Palindrome ").lower().replace(" ", "")
word = re.sub(r'[^a-z0-9]', '', word)
is_palindrome(word)