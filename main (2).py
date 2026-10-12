import random
real = random.randint(1, 100)
anwser = False
while not anwser:
    attempt = int(input())
    if abs(attempt - real) > 30:
        print("Frio")
    elif abs(attempt - real) > 20:
        print("Morno")
    elif abs(attempt - real) > 10:
        print("Quente")
    elif abs(attempt - real) >= 1:
        print("Muito quente")
    elif attempt == real:
        print("Chegou no Sol!")
        break
