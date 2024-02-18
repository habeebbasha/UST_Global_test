def word_frequency(line):
    words = line.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_frequency = sorted(frequency.items())

    return sorted_frequency


line = "which is better python 2 or python 3"
result = word_frequency(line)
print(result)
