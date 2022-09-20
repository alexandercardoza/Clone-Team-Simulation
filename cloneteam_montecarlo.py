import pandas as pd
import numpy as np
from random import random

# Gathering Base Statistics

print("Welcome to the Clone Team Simulator\n")
player = str(input("To begin, please enter the player's name: "))
print("Please enter the following stats\n")

ab = int(input("AB: "))
h = int(input("H: "))
doubles = int(input("2B: "))
triples = int(input("3B: "))
hr = int(input("HR: "))
singles = h - doubles - triples - hr
tb = singles + (doubles * 2) + (triples * 3) + (hr * 4)
bb = int(input("BB: "))
hbp = int(input("HBP: "))
sb = int(input("SB: "))
cs = int(input("CS: "))
so = int(input("SO: "))
sh = int(input("SH: "))
sf = int(input("SF: "))
gidp = int(input("GIDP: "))

stats = [ab, h, singles, doubles, triples, hr, tb, bb, hbp, sb, cs, so, sh, sf, gidp]

# Calculation of additional statistics needed to determine event probabilities
pa = ab + bb + hbp + sh + sf
atbats = ab + sh + sf
e = round(0.018 * atbats, 0)         # Historically, 1.8% of At Bats result in errors
oip = atbats - so - e - singles - doubles - triples - hr

# Calculation of Probabilities (Credit: Earnshaw Cook's "Percentage Baseball" & Jeff Sagarin)
so_prob = so / pa
bb_prob = bb / pa                      
hbp_prob = hbp / pa
e_prob = e / pa
lsingle_prob = .3 * (singles / pa)      # 30% of singles are long singles
msingle_prob = .5 * (singles / pa)      # 50% of singles are medium singles
ssingle_prob = .2 * (singles / pa)      # 20% of singles are short singles
sdouble_prob = .8 * (doubles / pa)      # 80% of doubles are short doubles
ldouble_prob = .2 * (doubles / pa)      # 20% of doubles are long doubles
triple_prob = (triples / pa)
hr_prob = (hr / pa)
gidp_prob = 0.5 * 0.538 * (oip / pa)     # 50% of ground outs are GIDP
normgb_prob = gidp_prob                  # 50% of ground outs are normal ground outs
ld_if_prob = 0.153 * (oip / pa)          # 15.3% of outs in play are line drives or infield flies
lfly_prob = 0.2 * 0.309 * (oip / pa)     # 20% of fly balls are long fly balls
mfly_prob = 0.5 * 0.309 * (oip / pa)     # 50% of fly balls are medium fly balls
sfly_prob = 0.3 * 0.309 * (oip /pa)      # 30% of fly balls are short fly balls

probs = [so_prob, bb_prob, hbp_prob, e_prob, lsingle_prob, msingle_prob, ssingle_prob, sdouble_prob, ldouble_prob, triple_prob, hr_prob, gidp_prob, normgb_prob, ld_if_prob, lfly_prob, mfly_prob, sfly_prob]

# Monte Carlo Simulation

probs_cumsum = list(np.cumsum(probs))

runs = pd.read_csv("runs.csv")
outs = pd.read_csv("outs.csv")
state_transitions = pd.read_csv("state_transitions.csv",dtype=object)

nsim = input("How many simulations do you want: ")

if (int(nsim) < 10000):
        print(" **** A higher number of simulations will provide a more accurate answer **** ")
        print(" **** Don't be afraid I can handle orders of magnitude higher **** ")

nruns = []

for i in range(int(nsim)):
	inning_state = '000'
	inning_outs = 0
	inning_runs = 0
	while (inning_outs <3):
		# First let's find what event happened
		coin_flip = random()
		if coin_flip < probs_cumsum[0]:
			event = 0 
		else:
			event = [i for i in range(len(probs_cumsum)) if coin_flip >= probs_cumsum[i] and coin_flip < probs_cumsum[i+1]][0]+1
		# How many runs happened
		inning_runs += runs[inning_state+'-'+str(inning_outs)][event]
		# How many outs were added 
		inning_outs += outs[inning_state+'-'+str(inning_outs)][event]
		# Finding the new state
		inning_state = str(state_transitions[inning_state][event])
	nruns.append(inning_runs)


print("The average number of runs/inning for a team of", player, "clones is: ", np.mean(nruns))
print("The average number of runs/game for a team of", player, "clones is:", 9 * np.mean(nruns))
