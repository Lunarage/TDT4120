

def longest_repeated_substring(dna, k):
    substrings = {}
    longest_substring = None
    for i in range(1, len(dna)):
        for j in range(len(dna) - i + 1):
            substring = dna[j:j + i]
            if substring in substrings:
                substrings[substring] += 1
            else:
                substrings[substring] = 1
            if substrings[substring] >= k:
                longest_substring = substring
    return longest_substring
