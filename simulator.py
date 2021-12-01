from simulate import *
from game import *
from agent import *

# agent1 = RandomAgent() 
# agent2 = RandomAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print(simulator.playGames(1000)) 
# print("random v random")  # 0.39 0.27 0.34 10,000

# agent1 = PerceptronAgent() 
# agent2 = RandomAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print(simulator.playGames(1000))
# print("percep vs random agent") # 0.6425 0.1189 0.2386 10,000 trials


# agent1 = AdvancedPerceptronAgent() 
# agent2 = AdvancedPerceptronAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print (simulator.playGames(1000))
# print ("adv percep vs adv percep agent") #0.9288 0.0612 0.01 5000 trials
#

# agent1 = MinimaxPruningAgent(1) 
# agent2 = RandomAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print simulator.playGames(1000) 
# print "minimax pruning 1 vs random agent" # 0.547 0.198 0.255 1000 trials
#
# agent1 = MinimaxPruningAgent(2) 
# agent2 = RandomAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print (simulator.playGames(500) )
# print ("minimax pruning 2 vs random agent" )# 0.508 0.23 0.262 500 trials


# agent1 = ExpectimaxAgent(2) 
# agent2 = RandomAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print (simulator.playGames(100) )
# print ("expectimax 2 vs random" )# 56.0 0.0 out of 56 did not finish running
#
# agent1 = ExpectimaxAgent(1) 
# agent2 = RandomAgent() 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print (simulator.playGames(100) )
# print ("expectimax 1 vs random" )# 0.984 0.01 0.006 1000 trials


agent1 = ExpectimaxAgent(1) 
agent2 = PerceptronAgent() 
simulator = UltimateTicTacToeSimulator(agent1, agent2) 
print (simulator.playGames(100)) 
print ("expectimax 1 vs perceptron") # 0.866666666667 0.0893333333333 0.044 750 trials
#

# agent1 = ExpectimaxAgent(1) 
# agent2 = MinimaxPruningAgent(1) 
# simulator = UltimateTicTacToeSimulator(agent1, agent2) 
# print (simulator.playGames(100)) 
# print ("expectimax 1 vs minimax pruning 1") # 0.99 0.008 0.002 500 trials

