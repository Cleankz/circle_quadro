import random
def ConquestCampaign(N,  M,  L, battalion = []):
    N1 = N
    N2 = M
    m = []
    for z in range(N1):
        row = []
        for q in range(N2):
            z = random.randint(0,2)
            row.append(z)
        m.append(row)
    for i in range(0,len(battalion),2):
        for x in range(len(m)):
            if battalion[i] == x:
                for y in range(len(m[x])):
                    if battalion[i+1] == y:
                        m[x][y] = 10
                        break
    day = 1
    for a in range(len(m)):
        for b in range(len(m[a])):
            try:
                if m[a][b] == 10:
                    m[a][b-1] = 10
                    m[a][-b-1] = 10
                    m[-a][b] = 10
                    m[a-1][b] = 10
                    day = day +1
                    break
                    #m[-a][b] = 10
            except IndexOutOfRange:
                pass
        for e in range(len(m)):
            for r in range(len(m[e])):
                if m[e][r] == 10:
                    m[e][r-1] = 10
                    m[e][-r-1] = 10
                    m[-e][r] = 10
                    m[e-1][r] = 10
                    break
    return day