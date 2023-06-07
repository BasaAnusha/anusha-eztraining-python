class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[]
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent==i:
            return i
        return self.find(parent,parent[i])
    def apply_union(self,parent,rank,x,y):       
        #attack smaller rank tree under high rank tre
        #if both same make the any one as a  parent and make its a rank
          print("rank",rank)
          xroot=self.find(parent,x)
          yroot=self.find(parent,y)
          if rank[xroot]<rank[yroot]:
                parent[xroot]=yroot
          elif rank[xroot]>rank[yroot]:
                parent[yroot]=xroot
          else:
                parent[yroot]=xroot
                rank[xroot]+=1
        #applying krushkhal algorithm
    def kruskal_algo(self):
            result =[]
            i,e=0,0
            self.graph=sorted(self.graph,key=lambda item:item[2])
            parent=[]
            rank=[]
            for node in range(self.V):
                print("node",   node)
                print()
                parent.append(node)
                rank.append(0)
            print("parent",parent)
            print("key",key)
            while e< self.V -1:
                u,v,w=self.graph[i]
                print("U:",u,"v:",v,"w:",w)
                i=i+1
                x=self.find(parent,u)
                print("x:",x,"parent of u:",u)
                y= self.find(parent,v)
                print("y",y)
                if x!=y:
                    e=e+1
                    result.append([u,v,w])
                    self.apply_union(parent,rank,x,y)
            for u,v,weight in result:
                 print("%d - %d:  %d" %(u,v, weight))
g=Graph(6)
g.add_edge(0,1,4)
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(1,0,4)
g.add_edge(2,0,4)
g.add_edge(2,1,2)
g.add_edge(2,3,3)
g.add_edge(2,5,2)
g.add_edge(2,4,4)
g.add_edge(3,4,3)
g.add_edge(4,2,4)


g.add_edge(4,3,3)
g.add_edge(5,2,2)
g.add_edge(5,4,3)
g.kruskal.algo()



                      
