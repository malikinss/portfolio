'''
TODO: Write a function is_one_away(word1, word2) that takes two words word1 and word2 as arguments and returns True if the words are the same length and differ by exactly 1 character and False otherwise.
'''


def is_one_away(word1, word2):
    mismatches = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1

        return mismatches == 1

    return False



txt1 = input()
txt2 = input()


print(is_one_away(txt1, txt2))