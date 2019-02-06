f = open("Street_Centrelines.csv",'r')

def tup():
    for v in f:
       v = v.split(",")
       t = (v[2], v[4], v[6], v[7])
       print(t)

tuple()

