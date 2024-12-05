MULT = 13
for i in range(50):
    i += 1
    if i % 7 != 0:
        print("{} x {} = {}".format(i, MULT, i * MULT))