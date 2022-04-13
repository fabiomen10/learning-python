a = int(input('Enter the first value: '))
b = int(input('Enter the second value: '))
print(type(a))
# a = 10
# b = 5
sum = a + b
subtraction = a - b
multiplication = a * b
division = a / b
rest = a % b
#print(type(sum))
result = ('Sum: {sum}. \nSubtraction: {subtraction}. '
      f'\nMultiplication: {multiplication}'
        '\nDivision: {division}'
        '\nRest: {rest}'.format(sum=sum,
                                subtraction=subtraction,
                                rest=rest,
                                multiplication=multiplication,
                                division=division))
print(result)
#print('sum: ' + sum)
#print(subtraction)
#print('subtraction: ' + str(subtraction))
#print(multiplication)
#print(int(division))
#print (rest)
# x = '1'
# # sum2 = int(x) + 1
# # print(sum2)

