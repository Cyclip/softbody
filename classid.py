import random, string

chars = list(string.ascii_uppercase + string.digits)

def genID():
    return ''.join(random.choice(chars) for _ in range(4))