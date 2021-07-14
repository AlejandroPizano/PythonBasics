import random
from words import wordsEng,wordsSp
def choose_words():
    lenguage=input("1= Español/ 2= English ")
    if lenguage =="1":
        word = random.choice(wordsSp)
    else:
        word = random.choice(wordsEng)
    return word
def hangman():
    attemps=0
    word = choose_words()
    ans =list("_"*len(word))
    flag=True
    print(word)
    usedwords = set()
    while attemps<len(word)+5:
        print(*ans)
        letter = input("Input your letter guess\n").lower()
        attemps+=1
        if letter in word:
            for c,l in enumerate(word):
                if l == letter:
                    ans[c]=letter
        else:
            usedwords.add(letter)
            print(*usedwords)
        if(ans==list(word)):
            print(f"Winner, the answer was: {word}")
            flag = False
            break
    if flag:
        print(f"You loose, the answer was: {word} ")

hangman()