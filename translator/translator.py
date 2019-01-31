
import os
import sys
import string

def nb_to_label(nb) :
    return 'loop_' + string.ascii_letters[int(nb/52)%52] + string.ascii_letters[nb%52]

def mbf(readptr) :
    global file
    depth = 1
    readptr += 1
    while True :
        if readptr >= len(file) :
            print("didn't find matching bracket")
            return
        if file[readptr] == '[' :
            depth += 1
        elif file[readptr] == ']' :
            depth -= 1
        if depth == 0 :
            return readptr
        readptr += 1

def translator(start, stop) :
    global file
    global output
    global loop_count
    i = start
    while i < stop :
        if file[i] == '>' :
            output += '\n\tcall mempp'
        elif file[i] == '<' :
            output += '\n\tcall mempm'
        elif file[i] == "+" :
            output += '\n\tcall memoryp'
        elif file[i] == "-" :
            output += '\n\tcall memorym'
        elif file[i] == '.' :
            output += '\n\tcall print'
        elif file[i] == '[' :
            loop_name = nb_to_label(loop_count)
            loop_count += 1
            mb_index = mbf(i)
            output += '\n' + loop_name + ' :'
            output += '\n\tmov edx, [memp]'
            output += '\n\tcmp [memory+edx], byte 0'
            output += '\n\tje end_' + loop_name
            translator(i+1, mb_index)
            output += '\n\tjmp ' + loop_name
            output += '\nend_' + loop_name + ' :'
            i = mb_index + 1
            continue
        i += 1

if __name__ == '__main__' :
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    file = f.read()
    f.close()

    f = open('header.asm', 'r')
    output = f.read()
    f.close()

    loop_count = 0

    ########## CORE HERE ##########

    translator(0, len(file))

    ########## END CORE  ##########

    output += "\n\tcall end_prg"
    f = open(sys.argv[2], 'w')
    f.write(output)
    f.close()
    #os.system('make')
