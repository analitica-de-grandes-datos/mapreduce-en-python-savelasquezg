#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys
elements = {}
def cspaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def set_biggersmalleramount(elements, aelement):
    earray = aelement.split("*")
    if earray[0] in elements:
        elements[earray[0]] = elements.get(earray[0]) +  [int(cspaces(earray[1]))]
    else:
        elements[earray[0]] = [int(cspaces(earray[1]))]
    return elements

for line in sys.stdin:
    set_biggersmalleramount(elements, line)

for element, array in  elements.items():
    array = ','.join(str(v) for v in sorted(array))
    print(element + "	" + array)
