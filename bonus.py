"""
409. Longest Palindrome

Given a string text which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

For this question, letters are case-sensitive, for example, "Aa" is not considered a palindrome.
"""
from prompt_toolkit.key_binding.bindings.named_commands import uppercase_word


# Change this function so it works correctly

from collections import Counter
def longest_palindrome_length(text):
        characters_count = Counter(text)

        length = 0
        num_of_odd = False

        for count in characters_count.values():
            if count % 2 == 0:
                length = length + count
            else:
                length = length + count - 1
                num_of_odd = True

        if num_of_odd:
            length = length + 1

        return length



if __name__ == '__main__':
    test_cases = [('abccccdd', 7),      # dccaccd / dccbccd
                  ('a', 1),             # a
                  ('school', 3)]        # oso / oco / oho / olo

    for test_text, expected in test_cases:
        result = longest_palindrome_length(test_text)
        msg = 'Correct' if expected == result else 'Wrong'
        print(f'[{msg:7s}] longest_palindrome_length("{test_text}") should be {expected}')
