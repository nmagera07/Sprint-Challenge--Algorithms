'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    w = word.find("th")
    
    if w != -1:
        return 1 + count_th(word[w+2:])
    else:
        return 0





