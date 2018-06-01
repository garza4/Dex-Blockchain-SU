import setup
import network as net
# import ConsensusAlgorithm as ca
# import CommandLineWallets as clw
import networkx as nx

admin = setup.User("bin", 20, 10)

firstSUBank = setup.CentralBank(0)
firstSUBank.createCoins(1000000, "doge")


#print(firstSUBank)

bobby = setup.User("garza4", 20, 10)
daniel = setup.User("merrittD", 20, 10)

bobby.purchaseCoins(firstSUBank, 10, "doge")
print(bobby)

firstNode = net.Transaction.createTransaction(bobby, daniel, 5, 1.00, 501, "doge")
#secondNode = net.Transaction.createTransaction(bobby, daniel, 5, 2.00, 502, firstSUBank.listOfCoins["doge"])

#print(net.Transaction.G.has_node(firstNode))
print(bobby)
print(daniel)



"""
Bobby buys 10 doge coins and wants to send 5 to daniel in two different transactions


"""


