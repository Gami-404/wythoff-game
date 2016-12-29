from node import Node
from Waythff import Waythff


x = Waythff()
node = Node()
node.counter1 = input("Enter the first counter1 ?")
node.counter2 = input("Enter the first counter2 ?")
print "start :" + node.toString()
x.minimx(node, node.predectDepth(), Waythff.maxPlayer)