import random

def generate_random_numbers(n):
    return [random.randrange(n) for i in range(n)]

def shuffle(arr):
    random.shuffle(arr)
    return arr

__all__ = ['generate_random_numbers', 'shuffle']