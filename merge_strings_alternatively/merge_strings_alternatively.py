def merge_alternately(word1, word2):
    merged_arr = []
    longest_word = max(len(word1), len(word2))

    for i in range(longest_word):
        if i < len(word1):
            merged_arr.append(word1[i])
        if i < len(word2):
            merged_arr.append(word2[i])
    return "".join(merged_arr)

result = merge_alternately("abc", "pqr")
print(result)