def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] +=1
        else:
            words[i] =1
    return words


def most_repeat(words):
    max_word = ""
    max_freq = 0
    for word, freq in word.items():
        if freq < max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = "como quieres que te quiera si el que quiero que me quiera no me uiere como quiero que me quiera"
print(count_words(text))
print(most_repeated(count_words(text)))