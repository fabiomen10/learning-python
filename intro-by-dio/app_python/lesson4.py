 a = int(input('First bimester: '))
while a > 10:
    a = int(input('You mistyped. First bimester: '))
b = int(input('Second bimester: '))
while b > 10:
    b = int(input('You mistyped. Second bimester: '))
c = int(input('Third bimester: '))
while c > 10:
    c = int(input('You mistyped. Third bimester: '))
d = int(input('Fourth bimester: '))
while d > 10:
    d = int(input('You mistyped. Fourth bimester: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))

# note = int(input('Enter the note: '))
# while note > 10:
#     note = int(input('Invalid note. Enter the correct note: '))
#     print(note)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1
# a = int(input('Enter a value: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         rest = num % x
#         #print(x, rest)
#         if rest == 0:
#             div += 1
#     if div == 2:
#         print(num)
    #     print('The number {} is prime'.format(a))
    # else:
    #     print('The number {} is not prime'.format(a))

# a = int(input('Enter a number: '))
# div = 0
#
# for x in range(1, a+1):
#     rest = a % x
# #    print(rest)
#     print(x, rest)
#     if rest == 0:
# #        div = div + 1 (concatenation)
#         div += 1
# if div == 2:
#     print('The number {} is prime'.format(a))
# else:
#     print('The number {} is not prime'.format(a))

# for x in range(101):
#     print (x)