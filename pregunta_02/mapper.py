#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def pa(x):
    return x[3] + "*" + x[4]

for line in sys.stdin:
    result = line.split(',')
    print(pa(result))
