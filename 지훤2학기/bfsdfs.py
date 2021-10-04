#노드의 개수M 간선의 개수 m 탐색 시작 번호 v
n,m,v=map(int,input().split(' '))

graph=[]
#그래프 만들기
for _ in range(n+1):
    graph.append([0]*(n+1))
    

for _ in range(m):
    a,b=map(int,input().split(' '))
    graph[a][b]+=1
    graph[b][a]+=1

bfs=[]
temp=[v]
visited=[v]
while(temp):
    v=temp.pop()
    for _ in range(1,n+1):
        if(graph[v][_] and (_ not in visited)):
            bfs.append(_)
            graph[v][_]-=1
            graph[_][v]-=1
            temp.append(_)
