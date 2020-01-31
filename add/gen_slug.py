import random


def gen_slug():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    gened_slug = ''
    for i in range(0, 20):
        a = random.choice(alphabet)
        gened_slug = gened_slug + a
    return gened_slug