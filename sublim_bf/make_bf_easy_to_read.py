
import sys

file_name = sys.argv[1]
f = open(file_name, 'r')
file = f.read()
f.close()

print("#######INITIAL CODE#######\n" + file + "\n")

depth = 0

new_code = '\n'
for ptr in range(len(file)) :
    c = file[ptr]
    l =  new_code[-1]
    if c in '<>+-[].,' :
        if c in '<>' :
            if l in '<>' :
                new_code += c
            else :
                new_code += '\n' + '\t'*depth + c
        elif c in '+-' :
            if l in '+-' :
                new_code += c
            else :
                if l == '\n' :
                    new_code += c
                else :
                    new_code += ' ' + c
        elif c in '.,' :
            new_code += ' ' + c
        elif c == '[' :
            new_code += '\n' + '\t'*depth + c
            depth += 1
        else :
            depth -= 1
            new_code += '\n' + '\t'*depth + c

new_code = new_code[1:]

print("########FINAL CODE########\n" + new_code + "\n")

print("len input:", len(file))
print("len output:", len(new_code))


f = open(sys.argv[2], 'w')
f.write(new_code)
f.close()
