import random

maze = {}

def gen(x, c):
    if c == 0:
        x[0] = random.randint(0, 1)
        x[1] = random.randint(0, 1)
        x[2] = random.randint(0, 1)
        return

    for i in range(3):
        if random.random() < 0.7:  # 70% chance to continue growing
            x[i] = {}
            gen(x[i], c - 1)
        else:
            x[i] = random.randint(0, 1)  # 30% chance to end early with a value
    