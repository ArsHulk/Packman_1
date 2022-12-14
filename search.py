# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    st=util.Stack()   #stack=(coordinates,path)
    passedby=[]     #visited
    direction=[]    #hot to get to every state
    if(problem.isGoalState(problem.getStartState())):
        return direction
    st.push((problem.getStartState(),[])) #beggining
    while(True):
        if st.isEmpty():
            return []
        x,direction=st.pop() #position and path of current state
        passedby.append(x)
        if problem.isGoalState(x): #if goal is found end 
            return direction
        
        temp=problem.getSuccessors(x)
        for part in temp:
            if part[0] not in passedby:
                st.push((part[0],direction + [part[1]]))
    #util.raiseNotDefined()
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    st=util.Queue()
    passedby=[]
    direction=[]
    if(problem.isGoalState(problem.getStartState())):
        return direction
    st.push((problem.getStartState(),[]))
    while(True):
        if st.isEmpty():
            return []
        x,direction=st.pop()
        passedby.append(x)
        
        if problem.isGoalState(x):
            return direction

        temp=problem.getSuccessors(x)
        for part in temp:
            if part[0] not in passedby:
                if part[0] not in (sta[0] for sta in st.list):
                    st.push((part[0],direction + [part[1]]))
                
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    st=util.PriorityQueue()
    passedby=[]
    direction=[]
    if(problem.isGoalState(problem.getStartState())):
        return direction
    st.push((problem.getStartState(),[]),0)
    while(True):
        if st.isEmpty():
            return []
        x,direction=st.pop()
        passedby.append(x)
        
        if problem.isGoalState(x):
            return direction

        temp=problem.getSuccessors(x)
        oldPri=-1
        for part in temp:
            if part[0] not in passedby and part[0] not in (sta[2][0] for sta in st.heap):
                st.push((part[0],direction + [part[1]]),problem.getCostOfActions(direction + [part[1]]))      
            elif part[0] not in passedby:
                if part[0] in (sta[2][0] for sta in st.heap):
                    for sta in st.heap:
                        if sta[2][0] == part[0]:
                            oldPri = problem.getCostOfActions(sta[2][1])
                        newPri = problem.getCostOfActions(direction + [part[1]])
                        if oldPri > newPri and oldPri!=-1:
                            st.update((part[0],direction + [part[1]]),newPri)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    st=util.PriorityQueue()
    passedby=[]
    direction=[]
    st.push((problem.getStartState(), []), 0)
    if(problem.isGoalState(problem.getStartState())):
        return []
    while(True):
        if st.isEmpty():
            return []
        x,direction=st.pop()
        if x in passedby:
            continue
        passedby.append(x)
        if problem.isGoalState(x):
            return direction
        temp=problem.getSuccessors(x)
        for part in temp:
            if part[0] not in passedby:
                    st.push((part[0],direction + [part[1]]),heuristic)




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
