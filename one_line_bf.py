
import sys

file_name = sys.argv[1]
f = open(file_name, 'r')
file = f.read()
f.close()


new_code = ''
for letter in file :
    if letter in '<>+-[].,' :
        new_code += letter

print("#######INITIAL CODE#######\n", file, "\n")

print("########FINAL CODE########\n", new_code, "\n")

print("len input:", len(file))
print("len output:", len(new_code))

f = open(sys.argv[2], 'w')
f.write(new_code)
f.close()
