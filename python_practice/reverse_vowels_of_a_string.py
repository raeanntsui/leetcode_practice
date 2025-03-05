def reverse_vowels(string):
    vowels = 'aeiouAEIOU'
    string = list(string)
    i, j = 0, len(string) - 1

    while i < j:
        if string[i] not in vowels:
            i += 1
            continue
        if string[j] not in vowels:
            j -= 1
            continue

        #swap
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1

    return "".join(string)
    
result = reverse_vowels("leetcode")
print(result)