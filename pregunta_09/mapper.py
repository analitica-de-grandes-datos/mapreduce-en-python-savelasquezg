#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def cspaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    x = x.replace("\t", "")
    return x

def pa(x):
    return   cspaces(x[2]) + ";"+  cspaces(x[0])+ ";" + cspaces(x[1])  
    #return   int(cspaces(x[2]))


for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('   ')
    print(pa(result))
