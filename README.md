# World Cup 2026 Predictor: Argentina vs England

A simple Python tool that usesPoisson Distribution to predict the winner of the World Cup 2026 semi-final and calculate the betting odds.

# What this project does
Instead of guessing, this project uses past data from the tournament to:
1. Calculate how many goals **Argentina** and **England** are expected to score.
2. Find the probability of every possible score (e.g., 1-1, 2-0, 0-1).
3. Convert these probabilities into **Betting Odds** (just like bookmakers do!).

---

## How it works
The prediction is based on the **Poisson Distribution** (a classic math formula used in sports analytics to predict rare events like goals).

We calculate the odds using a simple rule:
**Odds = 1 / Probability**

---

## 💻 How to use it

### 1. Install NumPy and SciPy
You only need two standard Python libraries. Install them via your terminal:
```bash
pip install numpy scipy
