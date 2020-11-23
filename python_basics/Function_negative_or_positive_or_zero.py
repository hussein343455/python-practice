def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 3,4,1,30, 1]:
    print(x,"is ",sign(x))
# Prints "negative", "zero", "positive"