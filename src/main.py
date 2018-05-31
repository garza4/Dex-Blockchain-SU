import setup
import network as net
# import ConsensusAlgorithm as ca
# import CommandLineWallets as clw
import networkx as nx

fakeTransactions1 = {}
fakeTransactions2 = {}
bobby = setup.User("garza4", 10, 20, 10, fakeTransactions1)
daniel = setup.User("merrittD", 0, 20, 10, fakeTransactions2)
firstNode = net.Transaction.createTransaction(bobby, daniel, 5, 1.00, 501)
secondNode = net.Transaction.createTransaction(bobby, daniel, 5, 2.00, 502)

print(net.Transaction.G.has_node(firstNode))
print(bobby)
print(daniel)



"""
I am creating the users garza4 and merritD. Bobby has 10 coins and has two transactions with Daniel. Bobby sends 5 pirateCoin each time so at the end he has 0 pC and daniel has 10.
They both have privateKeys of 20 and public keys of 10. This will eventually be a generated process, but for the moment these were made up.


"""


