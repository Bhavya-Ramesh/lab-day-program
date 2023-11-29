def max_words(sentences):
    max_words=0
    for i in sentences:
        words=i.split()
        max_words=max(max_words,len(words))
        return max_words
sentences=eval(input("enter a string:"))
result=max_words(sentences)
print(result)
