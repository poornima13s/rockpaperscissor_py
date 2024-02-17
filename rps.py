import random
print("*************************************")
print("*  *PAPER*  *ROCK*   *SCISSOR*      *")
print("*************************************")
print(" lets start the game !!...")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
    if(ma>5):
        print("#############################")
        print("Total match:",ma)
        print("Human score:",hs)
        print("AI score:",cs)
        if(hs>cs):
            print("congrats you won")
        elif(cs>hs):
            print("AI won....better luck nxt tym")
        else:
            print("MATCH DRAW")
        print("##############################")
        break
    c=input("choose Paper->p Rock->r Scissor->s Stop->stop: ")
    if(c=="p"):
        print("Paper")
        point=10+random.randint(1,3)
        match point:
            case 11:
                ma=ma+1
                hs=hs+1
                print("human:paper","AI: Rock")
                print("match:",ma,"human score:",hs,"AI score:",cs)
                print("human wins","AI lost the ,mmatch")
                print("_______________________________-")
            case 12:
                ma=ma+1
                cs=cs+1
                print("human:paper","AI: scissor")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("human wins","AI won the match")
                print("_____________________________")
            case 13:
                ma=ma+1
                hs+hs+1
                cs=cs+1
                print("human:paper","AI: paper")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("match draw")
                print("______________________")
    elif(c=="r"):
        print("rock")
        point=20+random.randint(1,3)
        match point:
            case 21:
                ma=ma+1
                hs=hs+1
                print("human:paper","AI: Rock")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("human wins","AI lost the ,mmatch")
                print("_______________________________-")
            case 22:
                ma=ma+1
                cs=cs+1
                print("human:paper","AI: scissor")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("human wins","AI won the match")
                print("_____________________________")
            case 23:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("human:paper","AI: paper")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("match draw")
                print("______________________")
    elif(c=="s"):
        print("scissor")
        point=30+random.randint(1,3)
        match point:
            case 31:
                ma=ma+1
                hs=hs+1
                print("human:paper","AI: Rock")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("human wins","AI lost the ,mmatch")
                print("_______________________________-")
            case 32:
                ma=ma+1
                cs=cs+1
                print("human:paper","AI: scissor")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("human wins","AI won the match")
                print("_____________________________")
            case 33:
                ma=ma+1
                hs=hs+1
                cs=cs+1
                print("human:paper","AI: paper")
                print("match:",ma,"human score:",hs,"AI score",cs)
                print("match draw")
                print("______________________")
        print("Scissor")
    elif(c=="stop"):
        break
print("program end")