import pygame
r=[]
t=[]
y=[]
s,k=0,0
l = [[0 for i in range(9)] for j in range(9)]
def box(j,q):
    if j>=0 and j<=2:
        if (q)>=0 and (q)<=2:
            return 1
        if (q)>=3 and (q)<=5:
            return 2
        if (q)>=6 and (q)<=8:
            return 3
    if j>=3 and j<=5:
        if (q)>=0 and (q)<=2:
            return 4
        if (q)>=3 and (q)<=5:
            return 5
        if (q)>=6 and (q)<=8:
            return 6
    if j>=6 and j<=8:
        if (q)>=0 and (q)<=2:
            return 7
        if (q)>=3 and (q)<=5:
            return 8
        if (q)>=6 and (q)<=8:
            return 9
def delete(x):
    b=0
    for i in range(0,len(t)):
        if t[i]==x:
            a=i
            b=1
    if b==1:        
        del t[a]        
def show(l):
    for i in range(9):
        for j in range(9):
            print l[i][j],
            if (j+1)%3==0:
                print '|',
        print        
        if (i+1)%3==0:
            print "_______________________"
def find():
    b,q=0,2
    for i in range(0,k-2):
        if [j-1,i] not in x:
            a=i
            b=1
            q=1
    while 1:
        if b!=1:
            for i in range(8,-1,-1):
                if [j-q,i] not in x:
                    a=i
                    b=1
                    break
        if b==1:
            break
        q=q+1    
                    
    return [a,j-q]        
def check(t):
    p=t
    if p+[i] in y:
        return False
    else:
        return True
    
for i in range(9):
    for j in range(9):
        l[i][j]=' '
       
        
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red = ( 255,   0,   0)
blue = (   0,   0, 255)

pygame.init()
    
size = (550, 550)
screen = pygame.display.set_mode(size)
     
pygame.display.set_caption("Sudoku")
     
done = False

clock = pygame.time.Clock()

width = 50
height = 50



font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 35)

key = '0'
solve = 0
flag = 0

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            n = (pos[0] - 50) / width
            m = (pos[1] - 50) / height
            if m in range(9) and n in range(9):
                flag = 1
            elif m == 0 and n in [11, 12]:
                solve = 1
            else:
                flag = 0
                
        if event.type == pygame.KEYDOWN and solve == 0:
            if event.key == pygame.K_0:
                key = '0'
            elif event.key == pygame.K_1:
                key = '1'
            elif event.key == pygame.K_2:
                key = '2'
            elif event.key == pygame.K_3:
                key = '3'
            elif event.key == pygame.K_4:
                key = '4'
            elif event.key == pygame.K_5:
                key = '5'
            elif event.key == pygame.K_6:
                key = '6'
            elif event.key == pygame.K_7:
                key = '7'
            elif event.key == pygame.K_8:
                key = '8'
            elif event.key == pygame.K_9:
                key = '9'
            elif event.key == pygame.K_RETURN:
                print "Input Over"
                done = True
            if flag == 1:
                l[m][n] = int(key)
            
    # --- Drawing code should go here
 
    screen.fill(white)

    #Question
    '''for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num = font2.render(str(grid[i][j]), True, blue)
                screen.blit(num, [width * (j + 0.4) + 50, height * (i + 0.3) + 50])'''

    for i in range(9):
        for j in range(9):
            if l[i][j] != ' ':
                num = font2.render(str(l[i][j]), True, red)
                screen.blit(num, [width * (j + 0.4) + 50, height * (i + 0.3) + 50])
            pygame.draw.rect(screen, black, [50 + width * j, 50 + height * i, width, height], 1)
            
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, black, [50 + (3 * width) * j, 50 + (3 * height) * i, 3 * width, 3 * height], 3)

    pygame.draw.rect(screen, black, [550, 50, 50, 100], 2)
    
    pygame.display.flip()
        
    clock.tick(10)

d={}                                                                                
c={}                                                                                                                                          
b={}
x=[]

for i in range(1,10):
    d[i]=range(1,10)
    c[i]=range(1,10)
    b[i]=range(1,10)
    
for i in range(1,10):
    for j in range(9):
        for k in range(9):
            if l[j][k]==i:
                b[box(j,k)].remove(i)
                
for i in range(9):    
    for j in range(9):
        if l[i][j]!=' ':
            d[i+1].remove(l[i][j])
            c[j+1].remove(l[i][j])
            x.append([i,j])
            
i,j,k,e=1,1,1,0    

while j<10:

    while k<10:

        if (i in d[j]) and (i in c[k]) and (i in b[box(j-1,k-1)]) and (l[j-1][k-1]==' ') and (check(t)):
            l[j-1][k-1]=i
            c[k].remove(i)
            d[j].remove(i)
            b[box(j-1,k-1)].remove(i)
            t=t+[i]
            y.append([0]*len(t))
            for z in range(0,len(t)):
                y[len(y)-1][z]=t[z]
            k=k+1
            i=1
            a=0
            
        elif l[j-1][k-1]!=' ':
            t=t+[l[j-1][k-1]]
            y.append([0]*len(t))
            for z in range(0,len(t)):
                y[len(y)-1][z]=t[z]
            k=k+1
            
        else:
            i+=1
            
        if k>=10:
            break
        
        if i>=10:              
            if k>=2:
                if k>=3 and [j-1,k-2] in x:
                    d[find()[1]+1].append(l[find()[1]][find()[0]])
                    c[find()[0]+1].append(l[find()[1]][find()[0]])
                    if (j-1)!=find()[1]:
                        for e in range(find()[1]+1,j-1):
                            for u in range(8,-1,-1):
                                delete(l[e][u])
    
                        for e in range(0,k-1):
                            delete(l[j-1][e])
                            
                        for e in range(8,find()[0]-1,-1):
                            delete(l[find()[1]][e])
                            
                    for e in range(k-1,find()[0]-1,-1):
                        delete(l[find()[1]][e])
                       
                    b[box(find()[1],find()[0])].append(l[find()[1]][find()[0]])
                    l[find()[1]][find()[0]]=' '
                    e=find()
                    k=find()[0]+1
                    i=1
                    j=e[1]+1
                elif [j-1,k-2] in x:
                    d[find()[1]+1].append(l[find()[1]][find()[0]])
                    c[find()[0]+1].append(l[find()[1]][find()[0]])
                    b[box(find()[1],8)].append(l[find()[1]][find()[0]])
                    if (j-1)!=find()[1]:
                        for e in range(find()[1]+1,j-1):
                            for u in range(8,-1,-1):
                                delete(l[e][u])
                        for e in range(0,k-1):
                            delete(l[j-1][e])
                        for e in range(8,find()[0]-1,-1):
                            delete(l[find()[1]][e])
                    for e in range(k-1,find()[0]-1,-1):
                        delete(l[find()[1]][e])
                    l[find()[1]][find()[0]]=' '
                    e=find()
                    k=find()[0]+1
                    j=e[1]+1
                    i=1
                   
                else:
                    d[j].append(l[j-1][k-2])
                    c[k-1].append(l[j-1][k-2])
                    b[box(j-1,k-2)].append(l[j-1][k-2])
                    delete(l[j-1][k-2])
                    l[j-1][k-2]=' '
                    k-=1
                    i=1 
                    
            elif k==1:
                if [j-2,8] in x:
                    d[find()[1]+1].append(l[find()[1]][find()[0]])
                    c[find()[0]+1].append(l[find()[1]][find()[0]])
                    b[box(find()[1],find()[0])].append(l[find()[1]][find()[0]])
                    if (j-1)!=find()[1]:
                        for e in range(find()[1]+1,j-1):
                            for u in range(8,-1,-1):
                                delete(l[e][u])
                        for e in range(0,k-1):
                            delete(l[j-1][e])
                        for e in range(8,find()[0]-1,-1):
                            delete(l[find()[1]][e])
                    for e in range(k-1,find()[0]-1,-1):
                        delete(l[find()[1]][e])    
                    l[j-2][find()[0]]=' '
                    e=find()
                    k=find()[0]+1
                    i=1
                    j=e[1]+1
                    
                elif j!=1:
                    d[j-1].append(l[j-2][8])
                    c[9].append(l[j-2][8])
                    b[box(j-2,8)].append(l[j-2][8])
                    delete(l[j-2][8])
                    l[j-2][8]=' '
                    k=9
                    i=1
                    j-=1
                    
                else:
                    d[j].append(l[j-1][k-1])
                    c[1].append(l[j-1][k-1])
                    delete(l[j-1][k-1])
                    b[box(0,0)].append(l[j-1][k-1])
                    l[0][0]=' '
                    i=1
                              
    j+=1
    k=1
done=False    
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
    for i in range(9):
            for j in range(9):
                if [i,j] not in x:
                    num = font2.render(str(l[i][j]), True, blue)
                    screen.blit(num, [width * (j + 0.4) + 50, height * (i + 0.3) + 50])
                else:
                    num = font2.render(str(l[i][j]), True, red)
                    screen.blit(num, [width * (j + 0.4) + 50, height * (i + 0.3) + 50])       
                pygame.draw.rect(screen, black, [50 + width * j, 50 + height * i, width, height], 1)
                
            
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, black, [50 + (3 * width) * j, 50 + (3 * height) * i, 3 * width, 3 * height], 3)

    pygame.draw.rect(screen, black, [550, 50, 50, 100], 2)
    
    pygame.display.flip()
        
    clock.tick(10)

pygame.quit()
