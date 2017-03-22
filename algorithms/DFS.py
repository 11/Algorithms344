def init_graph():
    a = ['a', [], False]
    b = ['b', [], False]
    c = ['c', [], False]
    d = ['d', [], False]
    e = ['e', [], False]

    a[1].append(b)
    a[1].append(c)
    b[1].append(c)
    b[1].append(e)
    e[1].append(d)

    return a

#aka, in-order traversal
def DFS(node):
    
    if node[2] == False:

        #print node
        print(node[0])

        #seen = True
        node[2] = True
        
        for i in node[1]:
            DFS(i)


if __name__ == '__main__':
    root = init_graph()
    DFS(root)
