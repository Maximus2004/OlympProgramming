def fill(num, typ, index):
    if typ == 1:
        pict = [2]*(m-)
            
    elif typ == 0:
        for i in range(n):
            pict[i][num] = 1

def check(): #проверяем, что на начальном этапе может быть известно
    for i in range(maxsz):
        for j in range(2):
            l = descript[i][j][0]
            if l == 1:
                lenn = descript[i][j][1]
                if lenn > m//2:
                    fill(i,j,lenn)                    

t = int(input())
for q in range(t):
    #ввод данных
    maxsz = 100
    maxbl = (maxsz+1)//2
    n, m = map(int, input().split())
    descript = []
    need_refresh = []
    for i in range(maxsz):
        descript.append([0,0])
        need_refresh.append([0,0])
    for i in range(n):
        temp = list(map(int, input().split()))
        descript[i][1] = temp #1 - если строка под номером i, temp=сколько в этой строке блоков и их длины
        need_refresh[i][1] = True
    for i in range(n):
        temp = list(map(int, input().split()))
        descript[i][0] = temp
        need_refresh[i][0] = True
    for i in range(len(descript)):
        print(descript[i])
    for i in range(len(need_refresh)):
        print(need_refresh[i])
    pict = [2]*n
    for i in range(n):
        pict[i] = [2]*m
    print(pict)
    sol_found = False


    
    

    #вывод решения
    for i in range(n):
        for j in range(m):
            print(pict[i][j], end=' ')
        print()
