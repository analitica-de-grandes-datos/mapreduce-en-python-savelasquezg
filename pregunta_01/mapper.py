#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def pamount(x):
    return x[2]

for line in sys.stdin:
    result = line.split(',')
    print(pamount(result))
