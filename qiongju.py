import linecache

ring=[{3,65,66,67,112,113},\
      {99,100,101,108,112,113},{65,94,97,98,99,113,},{65,66,90,92,93,94},{3,46,66,90,104,105},{3,45,46,67,96,102},{67,91,95,96,108,112},\
      {5,6,60,100,101,106},{11,59,60,98,99,100},{10,11,15,18,97,98},{15,32,54,93,94,97},{44,49,53,54,92,93},{13,44,64,90,92,105},\
      {13,14,37,40,104,105},{36,37,45,46,88,104},{45,87,88,102,114,117},{56,75,95,96,102,114},{56,78,81,85,91,95},{77,78,91,101,106,108},\
      {1,2,4,5,6,109},{4,5,58,59,60,61},{9,10,11,58,59,73},{9,10,17,18,33,34},{15,16,17,18,32,120},{32,52,53,54,55,120},\
      {48,49,50,51,52,53},{44,47,48,49,63,64},{12,13,14,43,63,64},{14,39,40,41,42,43},{35,36,37,38,39,40},{35,36,86,87,88,89},\
      {86,87,116,117,118,119},{75,103,114,115,116,117},{56,57,75,84,85,103},{80,81,82,83,84,85},{76,77,78,79,80,81},{1,6,76,77,106,107}]

def combinations(array, tuple_length, prev_array=[]):
    if len(prev_array) == tuple_length:
        return [prev_array]
    combs = []
    for i, val in enumerate(array):
        prev_array_extended = prev_array.copy()
        prev_array_extended.append(val)
        combs += combinations(array[i+1:], tuple_length, prev_array_extended)
    return combs

def choose(array):
    l=len(array)
    for i in range (1,l//2+1):
        for items in combinations(array,i):
            a = [i for i in array if i not in items]
            x1=set()
            x2=set()
            for x in items:
                x1=x1|x
            for y in a:
                x2=x2|y
            if len(x1&x2)==0:
                return 0
    return 1

x=input("请输入环数:")
x=int(x)
res=[]
for item in combinations(ring,x):
    if choose(item)==1:
        x=set()
        for y in item:
            x=x|y
        res.extend([x])
file=open('C.xyz', 'w')
for item in res:
    q=str(len(item))
    file.write(q)
    file.write("\n")
    file.write("\n")
    for a1 in item:
        file.write(linecache. getline('石墨烯.txt',a1))
file.close()
