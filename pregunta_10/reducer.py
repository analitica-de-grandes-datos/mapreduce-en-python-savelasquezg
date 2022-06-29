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
    if element_array[0] in elements:
        elements[element_array[0]] = elements.get(element_array[0]) +  [int(clear_spaces(element_array[1]))]
    else:
        elements[element_array[0]] = [int(clear_spaces(element_array[1]))]
    return elements

for line in sys.stdin:
    set_biggersmalleramount(elements, line)

for element, array in  elements.items():
    array = ','.join(str(v) for v in sorted(array))
    print(element + "	" + array)
