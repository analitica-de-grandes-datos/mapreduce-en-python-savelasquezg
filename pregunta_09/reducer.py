#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
bp = []
countelementscol3 = 0


def set_bp(apurposes, aelement):
    aelement = aelement.replace("\n", "")
    bp.append(aelement)
    return apurposes


def sortByColumn3(element):
    return int(element.split(";")[0])


for line in sys.stdin:
    set_bp(bp, line)

bp.sort(key=sortByColumn3)

for purpose in bp:
    countelementscol3 = countelementscol3 + 1
    element = purpose.split(";")
    print(element[1]+ "   " + element[2] + "   " + element [0])
    if countelementscol3 > 5:
        break
