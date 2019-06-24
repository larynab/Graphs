import random
#Using the util from the original part 1: graph proves a vital component/resource
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        # create a lits of all possible friendship combinations
        combinations = []
        for i in range(1, numUsers + 1):
            for j in range(1, numUsers + 1):
                # avoid friend with self and duplicate friendships
                if i != j and i < j:
                    combinations.append([i, j])
        # randomise the cominations list
        random.shuffle(combinations)
        # take the first numUssers * avgFriendships number of friendships // 2
        friendship_list = combinations[:numUsers * (avgFriendships // 2)]
        # Add users
        for i in range (1, numUsers + 1):
            self.addUser(i)
        # Create friendships
        for friendship in friendship_list:
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # initialise an empty dictionary of visited vertices
        visited = {}
        # initialise a queue data structure and append userID as the first item in a list
        q = Queue()
        q.enqueue([userID])
        # while the queue is not empty, keep traversing
        while q.size():
            # dequeue the next path and store it in a variable
            p = q.dequeue()
            # grab the last vertex from the path
            v = p[len(p)  - 1]
            # if the vertex has not already been visited, make a new dictionary key and assign it the current path
            if v not in visited:
                visited[v] = p
                # for each connected vertex in the vertex's set, add a copy of the current path with it appended on the end
                for next_vertex in self.friendships[v]:
                    # make a copy of the current path
                    p_copy = p[:]
                    # append the next_vertex to the path and enqueue
                    p_copy.append(next_vertex)
                    q.enqueue(p_copy)
        # return friend pathways
        return visited
             

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

