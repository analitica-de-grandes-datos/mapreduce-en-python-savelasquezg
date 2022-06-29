#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def cspaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x


def pa(x):
    return  cspaces(x[0]), cspaces(x[1]).split(",")

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('\t')
    number, array = pa(result) 
    for letter_array in array:
        print(letter_array + "*" + number)
