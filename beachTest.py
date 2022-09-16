
def getAdj(r,x,y):
    adj = [] # adjacent cells with respect to radius
    for i in range(1,r+1):
        adj.append([x-i, y])
        adj.append([x + i , y])
        adj.append([x, y-i])
        adj.append([x,y+i])
        adj.append([x-i,y-i])
        adj.append([x+i, y + i])
        adj.append([x-i,y+i])
        adj.append([x+i, y - i])
    return adj    

def helper(log, beach):
    r, x,y = log
    beach[x][y] = 1
    n = 0
    adj = getAdj(r,x,y)
    for dx,dy in adj:
        if dx >=0 and dx < len(beach) and dy >= 0 and dy < len(beach[0]) and beach[dx][dy] == 1:
            n += 1
    return n      

def throws(bc, b, beach):
    i,j = bc
    adj = getAdj(b,i,j)
    m = 0
    for dx,dy in adj:
        if dx >=0 and dx < len(beach) and dy >= 0 and dy < len(beach[0]) and beach[dx][dy] != "V":
            if beach[dx][dy] == 1:
                m += 1
            beach[dx][dy] = "V"  #marking as visited so that next time no adjcent to the current radius wont check  
    return m

def countPits(h, w, logs, b):
    beach = [[0 for _ in range(h)] for _ in range(w)]
    noOfPoints = len(logs) 
    for k in range(len(logs)):
        noOfPoints -= helper(logs[k], beach)
    remaingHoles = noOfPoints
    ballCords = [(0,0), (b,0), (0,b), (b,b)] # maintaing possible coordinate of ball which refers to b in ths function
    t = 0
    for bc in ballCords:
        if remaingHoles > 0:
            t += 1
            remaingHoles -= throws(bc, b, beach)
    return noOfPoints,t

logs = [[2,9,9], [3,9,0], [1,9,8]]
print("no of Holes :", countPits(10, 10, logs, 5)[0])
print("the number of points to throw :", countPits(10, 10, logs, 5)[1])


