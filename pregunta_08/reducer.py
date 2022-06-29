#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
sum = {}
count = {}

def set_bsmalleramount(sum, count, aelement):
    earray = aelement.split("*")
    sum[earray[0]] = float(sum.get(earray[0]) or 0) + float(earray[1])
    count[aelement[0]] = float(count.get(aelement[0]) or 0)  +1 
    return sum, count

for line in sys.stdin:
    set_bsmalleramount(sum, count, line)

for max, min in zip(sum.items(), count.items()):
    print( max[0] + "	" + str(max[1]) + "	" + str(float(max[1])/float(min[1])) )
