# python program to implement a function to check whether a text is pangram or not

# function to check whether a text is pangram or not
def pangram(text):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    text_set = set(text)
    
    if not alphabet_set - text_set:
        print('pangram')
    else:
        print('Not pangram')
        
    
text = 'the quick brown fox jumps over the lazy dog'

pangram(text)