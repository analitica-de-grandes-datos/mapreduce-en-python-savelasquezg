#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def cspaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

  
def pa(x):
    return cspaces(x[1].split("-")[1])

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('   ')
    print(pa(result))
