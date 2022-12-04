
def turn_number_perfume():
    a = 0
    while True:
        a += 1
        yield a

def turn_number_medicine():
    b = 0
    while True:
        b += 1
        yield b

def turn_number_cosmetics():
    c = 0
    while True:
        c += 1
        yield c

num_perfume = turn_number_perfume()
num_medicine = turn_number_medicine()
num_cosmetics = turn_number_cosmetics()




