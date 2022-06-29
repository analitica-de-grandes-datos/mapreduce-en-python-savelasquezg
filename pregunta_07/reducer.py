#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
bp = {}


def set_bp(dictionary_purposes, aelement):
    aelement = aelement.replace("\n", "")
    letter = aelement.split(" ") [0]
    if  str(dictionary_purposes.get(letter) or "") == "":
        dictionary_purposes[letter] =    str(dictionary_purposes.get(letter) or "") + aelement.split(" ") [1]
    else:
        dictionary_purposes[letter] =    str(dictionary_purposes.get(letter) or "") +  "*" + aelement.split(" ") [1]
    return dictionary_purposes


def sortByColumn3(element):
    return int(element.split(";")[0])


for line in sys.stdin:
    set_bp(bp, line)


for purpose, values_and_dates in bp.items():
    elements = values_and_dates.split("*")
    elements.sort(key =sortByColumn3)
    bp[purpose] = elements
    for element in elements:
        print(purpose + "   " + element.split(";")[1] + "   " + element.split(";")[0] )
