
n = int(input())  # Read the number of scores
scores = list(map(int, input().split()))  # Read the scores as a list of integers

# Find the highest score
max_score = max(scores)

# Remove all occurrences of the highest score
while max_score in scores:
    scores.remove(max_score)

# Find the new highest, which is the runner-up score
runner_up_score = max(scores)
print(runner_up_score)