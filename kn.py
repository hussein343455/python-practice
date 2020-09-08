#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

# x=int(input())
# top=0;
# for i in range(x+1):
#     top=top+i
# print(top)

#---------------------------------------------------------------------------
#Modify the previous program such that only multiples of three or
#five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17   =60

# x=int(input())
# top=0;
#
# for i in range(x+1):
#     if( i%3==0 or i%5==0):
#         top=top+i
# print(top)

#---------------------------------------------------------------------------
#Write a program that asks the user for a number n and gives them the possibility to
#choose between computing the sum and computing the product of 1,…,n.

# x=int(input())
# y=input("for the sum please enter S \nor the product please enter P\n")
# b=2;
# result=1;
# y=y.lower()
# if y=="s":
#     b=1
# elif y=="p":
#     b=0
# for i in range(1,x+1):
#     if b==1 :
#         result=result+i
#     elif b == 0:
#         result=result*i
#     else:
#         break
# print(result)

#---------------------------------------------------------------------------
#Write a program that prints a multiplication table for numbers up to 12.

# for i in range(0,13):
#     for x in range(0,10):
#         res = x* i
#         print(x,' * ',i,' = ',res)
#     print("\n")
#---------------------------------------------------------------------------
#Write a program that prints all prime numbers.

# num = 143
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

#---------------------------------------------------------------------------
# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.

# def cheak():
#     if not trays:
#         trays.append(guess)
#     for i in trays:
#
#         if guess==i:
#             break
#     else:
#         trays.append(guess)
#         print(trays)
# number=31
# cont=0
# trays=[]
# while True:
#     guess=int(input())
#     if guess==number:
#         print("you win it is right")
#         break
#     elif guess<number:
#         print("Try agin it is Small :")
#     else:
#         print("Try agin it is Large :")
#     cheak()
# trays.append(guess)
# print("nice work you did ",len(trays),"trays")

#---------------------------------------------------------------------------
#Write a function that returns the largest element in a list
# def lar(x):
#     lg = x[0]
#     for i in x:
#         if lg < i:
#             lg = i
#     return lg
# x=[1,3,14,75,3,14,72]
# print(lar())

#or

# def lar(x):
#     return max(x)
# x=[1,3,14,75,3,14,72]
# print(lar(x))


#---------------------------------------------------------------------------
#Write function that reverses a list, preferably in place.

# def rev():
#     ind1=0;
#     ind2=len(x)-1;
#     for i in reversed(x):
#         swaper(ind1,ind2)
#         ind1=ind1+1;
#         ind2=ind2-1;
#         if ind1==ind2:
#             break
#     return
# def swaper(p1, p2):
#     x[p1], x[p2] = x[p2], x[p1]
# x=[1,3,14,75,3,14,72]
# rev()
# print(x)

#---------------------------------------------------------------------------
#Write a function that checks whether an element occurs in a list.
# def checks(u):
#     if x.count(u)==0:
#         print("not here")
#     else:
#         print("it is here ")
#
# x=[1,3,14,75,3,14,72]
# while True:
#     checks(int(input()))

#---------------------------------------------------------------------------
#WWrite a function that returns the elements on odd positions in a list.
# def checks():
#     top = 0
#     for i in x :
#         if i%2!=0:
#            top=top+1
#     return top
# x=[1,3,14,75,3,14,72]
# print(checks())
#---------------------------------------------------------------------------
#Write a function that tests whether a string is a palindrome.
