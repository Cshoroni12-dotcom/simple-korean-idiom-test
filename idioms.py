#hello reader! whoever you are, my college interviewer , just a friend, or even a random person in the internet or even my interviewer for a job
#i know that this is in korean which might make it hard to read, but i will give you clear comments for you guys to understand <3
#(this is my first actual project)
import random
live = 9 #sets the maximum lives ( tries ) in this case
heart = "\u2764"*live #this is a heart emoji and with live, this makes it so that it shows up like the minecraft health bar
hint = ['?','?','?','?'] #this works if you types more then one of the letters correctly (the spaces light up kinda like wordle)
result = False 
words = ['수구초심' , '맥수지탄' , '망양지탄' , '풍수지탄', '노심초사'] #words that will cycle
num = random.randint(0,4) #picks one random word
idiom = words[num] #sets the random word
while True: #starting loop!
    print(hint)
    print(f"남은 생명: {heart}")
    one = input("get the idiom! : ")
    if one == idiom[0]:
        hint[0] = one
        print(hint)
    if one == idiom[1]:
        hint[1] = one
        print(hint)
    if one == idiom[2]:
        hint[2] = one
        print(hint)
    if one == idiom[3]:
        hint[3] = one
        print(hint)
    else:    #if answer in wrong
        print("! nope, you got it wrong")
        live -= 1 #cuts out lives (health)
        heart = "\u2764"*live
    if live == 0:
        print(f"you lost, the correct idiom was {idiom}")
        break
    if ? not in hint:
        print("NICE you got it right")
    
