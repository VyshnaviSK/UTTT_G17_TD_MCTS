from simulate import *
from game import *
from agent import *

agent1 = RandomAgent()
agent2 = RandomAgent()
simulator = UltimateTicTacToeSimulator(agent1, agent2)
print(simulator.playGames(1000))
print("random v random")  # 0.39 0.27 0.34 10,000


#agent1 = ExpectimaxAgent(1)
#agent2 = PerceptronAgent()
#simulator = UltimateTicTacToeSimulator(agent1, agent2)
#print (simulator.playGames(100))
#print ("expectimax 1 vs perceptron") # 0.866666666667 0.0893333333333 0.044 750 trials

