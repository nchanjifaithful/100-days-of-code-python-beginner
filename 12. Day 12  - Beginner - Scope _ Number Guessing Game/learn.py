score = 10

def increase_enemies():
    print(f"Your present score is {score}")
    return score + 1

score = increase_enemies()
print(score)