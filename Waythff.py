import math
import random


class Waythff:
    # @type float  the Golden Ratio using in define golden position
    goldenRatio = (1 + math.sqrt(5)) / 2  # 1.618

    # @type boolean the max player flag using in minimx function
    maxPlayer = True

    # @type boolean the min player flag
    minPlayer = False

    # Ask for golden or save position is the heuristic search to use best next move
    # @param counter1 int is the first Counter in node
    # @param counter2 int is the second Counter in node
    # @return boolean true if is it golden position ,false otherwise
    def isSafe(self, counter1, counter2):
        if counter1 > counter2:
            for i in range(0, counter2 + 1):
                c2 = math.floor(self.goldenRatio * i)  # Small counter is floor @*i
                c1 = math.floor((self.goldenRatio + 1) * i)  # BIG counter is floor @**2*i
                if c1 == counter1 and c2 == counter2:
                    return True
        else:
            for i in range(0, counter1 + 1):
                c1 = math.floor(self.goldenRatio * i)  # Small counter is floor @*i
                c2 = math.floor((self.goldenRatio + 1) * i)  # BIG counter is floor @**2*i
                if c1 == counter1 and c2 == counter2:
                    return True
        return False

    # Playing max and min player in two Counters
    # @param node Node class was create in main program
    # @param depth int the expect of depth
    # @param player boolean the player flag
    # @return boolean flag if win player
    def minimx(self, node, depth, player):
        if depth == 0 or (node.counter1 == 0 and node.counter2 == 0):
            print "Game over"
            if not player:
                print "MAX Player win"
            else:
                print "Min Player win"
            return not player
        else:
            if player == Waythff.maxPlayer:
                print "MAX Player"
            else:
                print "Min Player"
            if self.selectGoldPositionPlaying(node):
                return self.minimx(node, depth - 1, not player)
            result = self.selectNormalPlaying(node)
            print node.toString() + result
            return self.minimx(node, depth - 1, not player)

    # select by basic rules in game
    # @param node Node class the current node
    # @return string description the playing  select to playing
    def selectNormalPlaying(self, node):
        # playing if one is zero
        if node.counter1 == 0:
            tmp = node.counter2
            node.counter2 -= node.counter2
            return " Select normal position by reduce counter2: " + str(tmp)
        elif node.counter2 == 0:
            tmp = node.counter1
            node.counter1 -= node.counter1
            return " Select normal position by reduce counter2: " + str(tmp)
        # playing if two counter equals
        if node.counter2 == node.counter1:
            tmp = node.counter2
            node.counter2 = 0
            node.counter1 = 0
            return " Select normal position by reduce two counters: " + str(tmp)
        # playing if any counter 1
        if node.counter1 == 1:
            node.counter1 -= 1
            return " Select normal position by reduce counter1: " + str(1)
        elif node.counter2 == 1:
            node.counter2 -= 1
            return " Select normal position by reduce counter2: " + str(1)
        # Normal playing by using random playing in three type in playing
        tmp = random.randint(1, 3)  # Get rand value form 1....3
        if tmp == 3:
            tmp = random.randint(1, node.counter1)
            if node.counter1 - tmp != node.counter2:
                node.counter1 -= tmp
                return " Select normal position by reduce counter1: " + str(tmp)
            else:
                tmp = 2
        if tmp == 2:
            tmp = random.randint(1, node.counter2)
            if node.counter2 - tmp != node.counter1:
                node.counter2 -= tmp
                return " Select normal position by reduce counter2: " + str(tmp)
            else:
                tmp = 1
        if tmp == 1:
            tmp = random.randint(1, node.min())
            node.counter1 -= tmp
            node.counter2 -= tmp
            return " Select normal position by reduce two counters: " + str(tmp)
    # select by basic rules in game
    # @param node Node class the current node
    # @return string description the playing  select to playing
    def selectGoldPositionPlaying(self, nodeName):
        for i in range(1, nodeName.counter1):
            if (nodeName.counter1 - i) != nodeName.counter2 and self.isSafe(nodeName.counter1 - i, nodeName.counter2):
                nodeName.counter1 -= i
                print nodeName.toString() + " Select Gold position by reduce counter1: " + str(i)
                return True
        for i in range(1, nodeName.counter2):
            if nodeName.counter1 != (nodeName.counter2 - i) and self.isSafe(nodeName.counter1, nodeName.counter2 - i):
                nodeName.counter2 -= i
                print nodeName.toString() + " Select Gold position by reduce counter2: " + str(i)
                return True
        for i in range(1, nodeName.min()):
            if self.isSafe(nodeName.counter1 - i, nodeName.counter2 - i):
                nodeName.counter2 -= i
                nodeName.counter1 -= i
                print nodeName.toString() + " Select Gold position by reduce Two counter: " + str(i)
                return True
        return False
