print('hello world!')

#for i in range(1, 10):
#    print(i)
def ds(x, esplion):
    assert x >= 0, 'x must >=0'
    assert esplion > 0, 'esplion must be positive'
    low = 0
    high = max(x, 1)
    guess = (low + high) / 2.0
    ctr = 1
    while abs(guess ** 2 - x) > esplion and ctr <= 100:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
    guess = (low + high) / 2.0
    ctr += 1
    assert ctr <= 100, 'not perfect square number!'
    print('number:', x, 'sqrt:', guess, 'Times:', ctr)
    return guess

x = float(input('x:'))
esplion = float(input('esplion:'))
print(ds(x, esplion))