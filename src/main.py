import setup
import network as net
# import ConsensusAlgorithm as ca
# import CommandLineWallets as clw
import networkx as nx

fakeTransactions = {}
bobby = setup.User(10, 20, 10, fakeTransactions)
daniel = setup.User(0, 20, 10, fakeTransactions)
G =nx.Graph()
firstNode = net.Transaction.createTransaction(bobby, daniel, 5, 1.00, 501)

