a = int(input('First bimester: '))
if a > 10:
    a = int(input('You mistyped. First bimester: '))
b = int(input('Second bimester: '))
if b > 10:
    b = int(input('You mistyped. Second bimester: '))
c = int(input('Third bimester: '))
if c > 10:
    c = int(input('You mistyped. Third bimester: '))
d = int(input('Fourth bimester: '))
if d > 10:
    d = int(input('You mistyped. Fourth bimester: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Some wrong note was typed')

# a = int(input('Enter with the first value: '))
# b = int(input('Enter with the second value: '))
# rest_a = a % 2
# rest_b = b % 2
# if rest_a == 0 or not rest_b > 0:
#
# # if rest_a == 0 and rest_b == 0:
#     print('An even value was entered')
# else:
#     print('No even value has been entered')

# a = int(input('Enter a value: '))
# rest = a % 2
# if rest == 0:
#     print('The value is ever')
# else:
#     print('The value is odd')

# a = int(input('First value: '))
# b = int(input('Second value: '))
# c = int(input('Third value: '))
# if a > b and a > c:
#     print('The greater value is {}'.format(a))
# elif b > a and b > c:
#     print('The greater value is {}'.format(b))
# else:
#     print('The greater value is {}'.format(c))
# print('End of program')