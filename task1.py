f = open("Street_Centrelines.csv",'r')

def tup():
    for v in f:
       v = v.split(",")
       t = (v[2], v[4], v[6], v[7])
       print(t)

def maintenance():
    h = dict()
    for f2 in f:
       f2 = f2.split(",")
       if f2[12] not in h:
         h[f2[12]] = 1
       else :
         h[f[12]] += 1
    print(h)

tuple()
maintenance()

