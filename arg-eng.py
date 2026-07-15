import numpy as np
import scipy.stats as stats

# lamda was calculated using team A expected goals scored * team B expected goals conceded *  average goals scored per match in the World cup 2026 
lambda_arg = 0.76
lambda_eng = 0.95


max_goals = 10
score_matrix = np.zeros((max_goals, max_goals))

for i in range(max_goals): # arg goals
    for j in range(max_goals): # eng goals
        prob_arg = stats.poisson.pmf(i, lambda_arg)
        prob_eng = stats.poisson.pmf(j, lambda_eng)
        score_matrix[i, j] = prob_arg * prob_eng


draw_prob = np.trace(score_matrix) 
arg_win_prob = np.sum(np.tril(score_matrix, -1)) 
eng_win_prob = np.sum(np.triu(score_matrix,1))

arg_win = 0
eng_win = 0
draw = 0

for i in range(max_goals):
    for j in range(max_goals):
        if i > j:
            arg_win += score_matrix[i, j]
        elif j > i:
            eng_win += score_matrix[i, j]
        else:
            draw += score_matrix[i, j]

odds_arg_win = 1 / arg_win
odds_draw = 1 / draw
odds_eng_win = 1 / eng_win

print("--------------------------------------------------")
print(f"Argentina Win: {odds_arg_win:.2f}")
print(f"Draw         : {odds_draw:.2f}")
print(f"England Win  : {odds_eng_win:.2f}")
print("--------------------------------------------------\n")




