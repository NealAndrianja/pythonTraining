sentence = input("Enter a sentence: ")

words = sentence.split()

word_frequency = {}

for word in words:
    word = word.lower()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(word_frequency)