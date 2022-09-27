# Clone Team Simulation

## Description
This program measures a baseball player's performance based on the runs scored by a hypothetical team made up of that player's clones. The user simply inputs the desired player's first and last name followed by the year of interest. The Clone Team Simulation then collects the necessary statistics to determine the performance of a clone team over the span of the desired amount of innings.

## Libraries Used
- Pandas
- Numpy
- Pybaseball (https://github.com/jldbc/pybaseball)

## Files
- cloneteam_montecarlo.py
  - Monte Carlo Simulation
- outs.csv 
  - Determines the amount of outs created by each event
- runs.csv 
  - Determine the amount of runs created by each event in a given state
- state_transitions.csv
  - Determines which state to transition to given the previous state and the event that occurs 
  
## Stat Abbreviations
AB: At Bat
<br />H: Hit
<br />2B: Double
<br />3B: Triple
<br />HR: Home Run
<br />BB: Walk
<br />HBP: Hit By Pitch
<br />SB: Stolen Base
<br />CS: Caught Stealing
<br />SO: Strikeout
<br />SH: Sacrifice Hit
<br />SF: Sacrifice Fly
<br />GIDP: Grounded Into Double Play


## Twitter
Follow @cozystats on Twitter for interesting baseball statistics and graphics
