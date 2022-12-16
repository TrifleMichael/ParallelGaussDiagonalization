import graphviz

dot = graphviz.Digraph('FoataTree')


from Calculator import *


# Loading verticies
ind = 0
for l in foataTree.layers:
    for eq in l:
        dot.node(str(eq.uniqueLabel), eq.equation.label)

# Creating edges
connections = []
for l1 in range(1, len(foataTree.layers)):
    for eq1 in foataTree.layers[l1]:
        for l2 in range(l1-1, -1, -1):
            for eq2 in foataTree.layers[l2]:
                if eq1.equation.isDependant(eq2.equation):
                    connections.append([str(eq2.uniqueLabel), str(eq1.uniqueLabel)])

# Minimising graph
markForRemoval = [False for i in range(len(connections))]
for i in connections:
    for j in connections:
        for ind, k in enumerate(connections):
            if i[1] == j[0] and i[0] == k[0] and j[1] == k[1]:
                markForRemoval[ind] = True

for ind, i in enumerate(connections):
    if not markForRemoval[ind]:
        dot.edge(i[0], i[1])

# Printing addition info
print("D =", DSet())
print("I =", ISet())
foataTree.printTree()

# Saving graph
dot.view()
