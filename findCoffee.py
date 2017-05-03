numRows, numColumns  = 6, 7
coffeeLocations = [(2,1),(5,4)]
walls = [(3,5),(3,3),(3,4),(5,1),(5,2),(6,5),(6,6),(6,7)]
DeskLocation = (3,7)
remainingDesks, adjs, Solutions, TempPaths = [],[],[],[]

for r in range(numRows+1):      #loads all desks into list 'remainingDesks'
    for c in range(numColumns+1):
        if (r,c) not in walls and r != 0 and c != 0:
            remainingDesks.append((r,c))

remainingDesks.remove(DeskLocation)


def FindAdjacentDesks(desk):  # will return a list of adjacent desks
    for d in remainingDesks:
        if (d[0] == desk[0] and (d[1] - desk[1] == 1 or d[1] - desk[1] == -1)) \
                or (d[1] == desk[1] and (d[0] - desk[0] == -1 or d[0] - desk[0] == 1)):
            adjs.append(d)
    return adjs

paths = [[DeskLocation]]    #all paths will start at my desk

while len(remainingDesks) != 0:     #loop ends when I've checked all desks
    for li in paths:    #iterate over all the paths in 'paths'
        last = li[-1]    #Get last element from 'li'
        adjs = []
        FindAdjacentDesks(last) #get 'adjs' list with all adjacent desks
        
        TempPaths = [TempPaths.append(li[:].append(a)) for a in adjs]
        '''for a in adjs:  #iterate over all adjacent cells and add each new path to 'TempPaths'
            temp = li[:]
            temp.append(a)
            TempPaths.append(temp)   #create a new path with each adjacent cell'''

    paths = TempPaths[:]    #After all new paths are in TempPaths, transfer them to 'paths'
    TempPaths = []

    for le in paths:
        if le[-1] in remainingDesks:
            remainingDesks.remove(le[-1])   #to avoid having the path backtrack
        if le[-1] in coffeeLocations:       #if I've reached the coffee machine,
            Solutions.append(le)            #add this path to the solutions list
            paths.remove(le)            #remove it so we stop adding to it

    if len(paths) == 0:     #when all paths have ended in coffee, stop the iteration
        break

distance = len(desks)
for s in Solutions:
    if len(s) < distance:   #find which of the solutions is the shortest
        distance = len(s)
        minPath = s

print('The shortest distance to coffee is ' + str(len(minPath)-1))

