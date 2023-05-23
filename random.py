import random
import time

ALLCHAR = "~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"?><MNBVCXZ`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

def singleRun():
    idx = [i for i in range(0,94)]
    random.shuffle(idx)
    correct = 0 
    for i in idx:
        print(ALLCHAR[i])
        print(time.time())        
        k = input()
        print(time.time())
        if k == ALLCHAR[i]:
            correct+=1
        
    incorrect = 94-correct
    print(correct,incorrect)

singleRun()