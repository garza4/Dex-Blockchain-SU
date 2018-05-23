import networkx as nx
from src.setup import *

class transaction:
#transactions are nodes so the graph will be made in the transaction class... I think...
    __G = nx.Graph()
    def __init__(self, sender, receiver, amount, transactionTime):
        __user = User()
        # get the sender and receiver to send money...
        self.sender = user.privateKey
        self.receiver = user.privateKey
        self.amount = amount
        self.transactionTime = transactionTime
        __from = Node(self, self.sender, self.receiver, self.transactionTime) #private instance of the node class
        __to = Node(self, self.receiver, self.sender, self.transactionTime)
        G.add_node(__from,1) #add one node for the sender (__from)
        G.add_node(_to,1)   #add one node for the receiver (__to)
        G.add_edge(__from, __to) #this will create a topographic graph, but is this what we want?
