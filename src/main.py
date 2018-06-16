import setup
import network  as net
# import ConsensusAlgorithm as ca
# import CommandLineWallets as clw
import networkx as nx
import time
import ConsensusAlgorithm as cA

"""
TODO:
    *need to implement a uniqueID generator
    *implment transaction validation of the mempool
    *create blocks - when to split/link more graphs (how to do with hashing?)
    *Research Merkle Tree - possible answer to hashing
    *work on GCS
    
    
    
    
"""





firstSUBank = setup.CentralBank(0)
firstSUBank.createCoins(1000000, "doge")
firstSUBank.createCoins(1000000, "garlicCoin")


#print(firstSUBank)

bobby = setup.User("garza4", 20)
daniel = setup.User("merrittD", 20)
alexander = setup.User("germany", 20)

alexander.purchaseCoins(firstSUBank, 2000, "garlicCoin")
bobby.purchaseCoins(firstSUBank, 10, "doge")

#bobby.put_up_stake(bobby.privateKey, 20)

firstNode = net.Transaction.createTransaction(bobby, daniel, 5, time.time(), 501, "doge")
secondNode = net.Transaction.createTransaction(bobby, daniel, 5, time.time(), 502, "doge")
thirdNode = net.Transaction.createTransaction(alexander, daniel, 1000, time.time(), 503, "garlicCoin")

#print(net.Transaction.G.has_node(firstNode))
#print(bobby)
#print(daniel)
#print(alexander)

net.Transaction.validateTransactions()
#print(firstNode)



"""
Bobby buys 10 doge coins and wants to send 5 to daniel in two different transactions, so by the end Bobby will have 0 doge coin

for the command line interface do commands work by linking key phrases to functions? 


"""




