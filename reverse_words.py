#!/usr/bin/env python3

'''
reverse a sentence
the start of the new sentence must be a capital
no other part of the sentence should be capital unless it is a name
the end of the sentense must contain the correct puctuation mark/s
'''
import string

def reverseSentence(sentence):
    
    # move sentence into a list
    forward_words = list(sentence.lower().split(" "))
    last_word = forward_words[-1]
    punc = "."
    for i in last_word:
        if i in string.punctuation:
            punc = i
    reverse_words = forward_words[::-1]
    reverse_words[0] = reverse_words[0].capitalize().rstrip()
    returnstr = " ".join(reverse_words) + punc
    
    return(returnstr)


if __name__ == "__main__":
    sentence = input("Enter a sentence to reverse: ")
    sentence = reverseSentence(sentence)
    print(f"The sentence reversed is {sentence}")
    