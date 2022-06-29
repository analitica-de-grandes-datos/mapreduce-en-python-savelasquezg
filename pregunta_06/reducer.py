#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
ba = {}
sa = {}

def set_bsmalleramount(ba, sa, aelement):
    earray = aelement.split("*")
    ba[earray[0]] = max(
        float(ba.get(earray[0]) or 0), float(earray[1]))
    sa[earray[0]] = min(
        float(sa.get(earray[0]) or 10000), float(earray[1]))
    return ba, sa

for line in sys.stdin:
    set_bsmalleramount(ba, sa, line)

for max, min in zip(ba.items(), sa.items()):
    print( max[0] + "	" + str(max[1]) + "	" + str(min[1]) )
