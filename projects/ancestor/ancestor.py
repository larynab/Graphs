#using amazing resources!
from graph import Graph
from util import Stack

# the family members will represent the nodes
# The parents will be the edges
family_member = 6
family = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [8,9], [11,8], [10,1]]

def earliestAncestor(family_member, family):
    g = Graph()

    # fammily = vertices
    all_members = []
    for pair in family:
        for ind in pair:
            if ind not in all_members:
                all_members.append(ind)
                g.add_vertex(ind)

    # with the pairs the parents will now be added to the child vertices
    for pair in family:
        g.add_edge(pair[1], pair[0])
    
    return ancestor_search(family_member, g)
    #just like the dft, through elimination, the end result will land on the smallest id 

def ancestor_search(family_member, family_graph):
    #Using stack method, adding the first node
    s = Stack()
    s.push([family_member])

    #empty set of visited vertices
    visited_verts = set()
    # initialize a compete paths list
    complete_paths = []

    # while the stack is not empty, keep traversing
    while s.size():
        # pop the next path and store it as a variable
        p = s.pop()
        # grab the last vertex from the path
        v = p[len(p) - 1]
        # if the vertex has not already been visited
        if v not in visited_verts:
            if len(family_graph.vertices[v]) == 0:
                complete_paths.append(p)
            # add the vortex to the visited set
            visited_verts.add(v)
            # for each connected vertex in the vertex's set, add a copy of the current path with it appended on the end
            for next_vertex in family_graph.vertices[v]:
                # make a copy of the current path
                p_copy = p[:]
                # append the next_vertex to the path and push to the stack
                p_copy.append(next_vertex)
                s.push(p_copy)

    # find the longest path
    longest_path = complete_paths[0]
    for path in complete_paths:
        # replace the cur longest_path if given path is longer
        if len(path) > len(longest_path):
            longest_path = path
        # also replace the cur longest_path if given path is same lenght but final ID is smaller
        if (len(path) == len(longest_path)) and (path[-1] < longest_path[-1]):
            longest_path = path
    # return the final ancestor in tthe longest path
    ans = longest_path[-1]
    if ans == family_member:
        return -1
    else:
        return ans

print(earliestAncestor(family_member, family))