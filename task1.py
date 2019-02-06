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
       else:
         h[f[12]] += 1
    print(h)

def street_owner():
    owner_list = f[11]
    final_list = []
    for a in f:
        a = a.split(",")
        if a[11] not in final_list:
            final_list.append(a[11])
    print(final_list)

tuple()
maintenance()
street_owner()

