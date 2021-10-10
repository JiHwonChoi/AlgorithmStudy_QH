#dfs:(graph, start)
def dfs(G:list,v:int)->list:
    visited=[]
    stack=[v,]
    
    #이상함
    while(stack):
        current=stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(G[current])
            print("This is: ", stack)
        
    return visited

#정점개수 N 엣지개수M 탐색시작 노드 번호V
n,m,v=map(int,input().split(' '))

#탐색할 그래프 
G=[[0]*(n+1) for _ in range(n+1)]
print(G)

#연결된 노드 입력
for _ in range(m):
    a,b=map(int,input().split(' '))
    G[a][b]=G[b][a]=1
    
print(dfs(G,v))