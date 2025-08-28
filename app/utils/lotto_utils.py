import random


def pick_numbers(combination: list | tuple, seed: str, k: int = 1):
    if k < 1:
        return -1
    random.seed(seed)
    res = random.sample(combination, k=k)
    return res if k > 1 else res[0]
