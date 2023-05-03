import matplotlib.pyplot as plt
from montecarlo.montecarlo import Die
from montecarlo.montecarlo import Game
from montecarlo.montecarlo import Analyzer

# create fair coin
fair_coin = Die(['H', 'T'])

# create unfair coin
unfair_coin = Die(['H', 'T'])
unfair_coin.change_weight('H', 5)

# play game with all fair dice
game1 = Game([fair_coin]*3)
game1.play(1000)
analyzer1 = Analyzer(game1)
jackpot1 = analyzer1.jackpot()
freq1 = jackpot1 / len(game1.results)
print(freq1)

# play game with 2 unfair dice and 1 fair die
game2 = Game([unfair_coin, unfair_coin, fair_coin])
game2.play(1000)
analyzer2 = Analyzer(game2)
jackpot2 = analyzer2.jackpot()
freq2 = jackpot2 / len(game2.results)
print(freq2)

# plot results in a bar chart
fig, ax = plt.subplots()
ax.bar(['All fair dice', '2 unfair dice and 1 fair die'], [freq1, freq2])
ax.set_ylabel('Relative frequency of jackpots')
plt.show()