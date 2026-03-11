import random
live = 9
heart = "\u2764"*live
hint = ['?','?','?','?']
result = False
words = ['수구초심' , '맥수지탄' , '망양지탄' , '풍수지탄', '노심초사']
num = random.randint(0,4)
idiom = words[num]
while True:
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
    else:
        print("! nope, you got it wrong")
        live -= 1
        heart = "\u2764"*live
    if live == 0:
        print(f"you lost, the correct idiom was {idiom}")
        break
    if ? not in hint:
        print("NICE you got it right")
