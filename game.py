import random

with open('words.txt','r') as f:
    word = random.choice(f.readlines())

tries = 3
word_answer = [letter for letter in word]
word_answer.pop() 
wordlist = ['_' for char in word_answer]
playing = True
print('Welcome to Hangman!')
while playing:
    blank = ''.join(wordlist)
    print('------------------------------')
    print('Tries:',tries) 
    print(blank)
    print('')
    word_input = input('Guess the letter: ')
    if word_input in word_answer and word_input not in wordlist:  
        print('')
        print('You are right!')
        print('')
        for char in enumerate(word_answer):
            if char[1] == word_input:        
                wordlist[char[0]] = word_input        
    else:
        print('')
        print('You are wrong')
        print('')
        tries -= 1 
        
    if tries <= 0:
        print('')
        print('Game Over!')
        print('')
        print('The word was',word)
        playing = False
    if wordlist == word_answer:
        print('You win!')
        print('')
        playing = False 
