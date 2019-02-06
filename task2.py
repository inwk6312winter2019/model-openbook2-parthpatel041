f = open("Bus_Stops.csv", 'r')
f = open("Street_Centerlines.csv", 'r')


def accessible(f):
    infolist=[]
    f.readline()
    for line in f:
       line=line.strip()
       infolist.append(line.split(','))

    return infolist

       
