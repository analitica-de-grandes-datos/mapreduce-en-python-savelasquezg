#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
bp = {}


def set_bp(dictionary_purposes, actual_element):
    actual_element = actual_element.replace("\n", "")
    dictionary_purposes[actual_element] = int(dictionary_purposes.get(actual_element) or 0) + 1 
    return dictionary_purposes

  
for line in sys.stdin:
    set_bp(bp, line)

for purpose, amount in bp.items():
    print(purpose + "	" + str(amount))
