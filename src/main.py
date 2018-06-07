import setup
import network  as net
# import ConsensusAlgorithm as ca
# import CommandLineWallets as clw
import networkx as nx
import time


firstSUBank = setup.CentralBank(0)
firstSUBank.createCoins(1000000, "doge")
firstSUBank.createCoins(1000000, "garlicCoin")


#print(firstSUBank)

bobby = setup.User("garza4", 20, 10)
daniel = setup.User("merrittD", 20, 10)
alexander = setup.User("germany", 20, 10)

alexander.purchaseCoins(firstSUBank, 2000, "garlicCoin")
bobby.purchaseCoins(firstSUBank, 10, "doge")

print(bobby)

firstNode = net.Transaction.createTransaction(bobby, daniel, 5, time.time(), 501, "doge")
secondNode = net.Transaction.createTransaction(bobby, daniel, 5, time.time(), 502, "doge")
thirdNode = net.Transaction.createTransaction(alexander, daniel, 1000, time.time(), 503, "garlicCoin")

#print(net.Transaction.G.has_node(firstNode))
print(bobby)
print(daniel)
print(alexander)

net.Transaction.validateTransactions()



"""
Bobby buys 10 doge coins and wants to send 5 to daniel in two different transactions, so by the end Bobby will have 0 doge coin


"""


