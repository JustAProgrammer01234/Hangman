import random

with open('words.txt','r') as f:
    word = random.choice(f.readlines())

tries = 3
word_answer = [letter for letter in word]
word_answer.pop()
wordlist = ['_' for char in word_answer]
playing = True
while playing:
    print('------------------------------')
    print('Tries:',tries) 
    print(wordlist)
    word_input = input('Guess the letter: ')
    if word_input in word_answer and word_input not in wordlist:  
        print('You are right!')
        for char in enumerate(word_answer):
            if char[1] == word_input:        
                wordlist[char[0]] = word_input        
    else:
        print('You are wrong')
        tries -= 1 
        
    if tries <= 0:
        print(wordlist)
        print('')
        print('Game Over!')
        print('')
        print('The word was',word)
        playing = False
    if wordlist == word_answer:
        print(wordlist)
        print('')
        print('You win!')
        print('')
        playing = False 
