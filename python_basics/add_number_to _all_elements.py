nums = [0, 1, 4, 3, 4]
squares = []
i=0;
for x in nums:
    squares.append(x++2)#append:apply the function in the() to all x's
print(squares)

########## OR  ###########
nums = [0, 1, 2, 3, 4]
squares = [x+2 for x in nums]#same as before
print(squares)