def remove_common_words(s1, s2):
    words_s1 = s1.split()
    words_s2 = s2.split()
    common_words = set(words_s1) & set(words_s2)
    result_s1 = ' '(word for word in words_s1 if word not in common_words)
    result_s2 = ' '(word for word in words_s2 if word not in common_words)
    return result_s1, result_s2
sentence1 = eval(input("enter a string:"))
sentence2 = eval(input("enter a string:"))
result_s1, result_s2 = remove_common_words(sentence1, sentence2)
print("Sentence 1 after removing common words:", result_s1)
print("Sentence 2 after removing common words:", result_s2)
