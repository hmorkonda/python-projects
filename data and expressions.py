# num1 = int(input('Enter first num: '))
# num2 = int(input('Enter second num: '))
#
# print( num1, '+' , num2,  '=', num1 + num2)
# print( num1, '-' , num2,  '=', num1 - num2)
# print( num1, '*' , num2,  '=', num1 * num2)
# print( num1, '/' , num2,  '=', format(num1 / num2, '.4f'))
# print( num1, '**' , num2,  '=', num1 ** num2)
# print( num1, '//' , num2,  '=', num1 // num2)
# print( num1, '%' , num2,  '=', num1 % num2)
#
# a = int(input('enter: '))
# if a >= 65:
#     print('yas')
# else:
#     print('no')

#
# var= input('enter words:  ')
# if var < 'Sun' and var < 'Moon':
#     print("yes")
# else:
#     print('NOO')
#
# name = input('enter name: ')
# if name == 'Silva' or name == 'Anderson':
#     print('yes')
# else:
#     print('no')

age = int(input('enter age: '))
cholesterol = int(input('enter cholesterol level: '))

if age <= 19:
    if cholesterol < 170:
        print('Healthy')
    else:
        print('not healthy')
elif age > 19:
    if cholesterol >= 125 and cholesterol <= 200:
        print('Healthy')
    else:
        print('not healthy')
else:
    print('you are gonna die soon')
