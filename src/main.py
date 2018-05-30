import setup
import network as net
# import ConsensusAlgorithm as ca
# import CommandLineWallets as clw
import networkx as nx

fakeTransactions = {}
bobby = setup.User("bobby", 10, 20, 10, fakeTransactions)
daniel = setup.User("daniel", 0, 20, 10, fakeTransactions)
firstNode = net.Transaction.createTransaction(bobby, daniel, 5, 1.00, 501)
secondNode = net.Transaction.createTransaction(bobby, daniel, 5, 2.00, 502)

print(net.Transaction.G.has_node(firstNode))


