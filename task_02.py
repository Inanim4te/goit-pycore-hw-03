import random

def get_numbers_ticket(min, max, quantity):
    if 1 <= min < max <= 1000 and quantity <= (max - min + 1):
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)
    else:
        return []