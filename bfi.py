
# > incremente le pointer
# < decremente le pointer
# + ajouter 1
# - retire 1
# . print le byte actuel
# , demande une entrée
# [ ouvre une boucle
# ] ferme la boucle

import sys

file_name = sys.argv[1]
f = open(file_name, 'r')
file = f.read()
f.close()

memory = [0] * 1000
mptr = 0

readptr = 0

while readptr < len(file) :
    c = file[readptr]
    if c == '>' :
        mptr += 1
    elif c == '<' :
        mptr -= 1
    elif c == '+' :
        memory[mptr] += 1
    elif c == '-' :
        memory[mptr] -= 1
    elif c == '.' :
        print(chr(memory[mptr]), end='')
    elif c == ',' :
        memory[mptr] = ord(input()[0])
    elif c == '[' :
        if memory[mptr] == 0 :
            depth = 1
            readptr += 1
            while True :
                if readptr >= len(file) :
                    print("didn't find matching bracket")
                    quit()
                if file[readptr] == '[' :
                    depth += 1
                elif file[readptr] == ']' :
                    depth -= 1
                if depth == 0 :
                    break
                readptr += 1
    elif c == ']' :
        if memory[mptr] != 0 :
            depth = -1
            readptr -= 1
            while True :
                if readptr < 0 :
                    print("didn't find matching bracket")
                    quit()
                if file[readptr] == '[' :
                    depth += 1
                elif file[readptr] == ']' :
                    depth -= 1
                if depth == 0 :
                    break
                readptr -= 1
    readptr += 1
