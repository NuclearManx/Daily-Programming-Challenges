"""
Given a string s and a list of words words, where each word is the same length, 
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], 
return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter
"""

def substring_index_calc(s, words):
    string_length = len(s)
    # No words in words.
    try:
        substring_length = len(words[0])
    except IndexError:
        return []
    substring_quantity = len(words)
    substring_indices = []

    # Could do error checking to make sure all givens are true e.g. all subtrings are equally sized.

    for i in range(string_length - substring_length):
        all_worlds_in_substr = True
        substring = s[i:i + (substring_length * substring_quantity)]

        for word in words:
            if word in substring:
                pass
            else:
                all_worlds_in_substr = False

        if all_worlds_in_substr:
            substring_indices.append(i)
            i += substring_length

    return substring_indices


def subtring_index_calc_tester(s, words, expected):
    starting_indices = substring_index_calc(s, words)
    print(f"String s '{s}' with list of words {words} has starting indices of {starting_indices}. Should be: {expected}.")

problem_example_one = "dogcatcatcodecatdog"
problem_example_one_words = ["cat", "dog"]
problem_example_one_answer = [0, 13]
subtring_index_calc_tester(problem_example_one, problem_example_one_words, problem_example_one_answer)

problem_example_two = "barfoobazbitbyte"
problem_example_two_words = ["dog", "cat"]
problem_example_two_answer = []
subtring_index_calc_tester(problem_example_two, problem_example_two_words, problem_example_two_answer)

ex3 = "dogcatcatflynnsmudgecatmarinadogcatwhat?"
ex3_words = ["cat", "dog"]
ex3_answer = [0, 29]
subtring_index_calc_tester(ex3, ex3_words, ex3_answer)

ex4_no_words = "dogcatcatcodecatdog"
ex4_no_words_words = []
ex4_no_words_answer = []
subtring_index_calc_tester(ex4_no_words, ex4_no_words_words, ex4_no_words_answer)

ex5_no_s = ""
ex5_no_s_words = ["cat", "dog"]
ex5_no_s_answer = []
subtring_index_calc_tester(ex5_no_s, ex5_no_s_words, ex5_no_s_answer)
