import random


def produce_characters(start=1, stop=82):
    return (random.randint(1,82) for item in range(1, 16))
