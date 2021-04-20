import re

def solution(S):
    S = " ".join(S.split()) # convert multiple spaces to single space
    max_len = 0
    sentences = re.split('\.|\?|!',S) # an array of all sentences
    for sentence in sentences:
        sentence.strip(' ')
        words_num = sentence.count(' ')
        if words_num + 1> max_len:
            max_len = words_num + 1
    return max_len

print(solution('Hey , its        me.'))