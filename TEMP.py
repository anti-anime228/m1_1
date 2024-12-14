'''1st program'''
print(9 ** 0.5 * 5)

'''2nd program'''
print(9.99 > 9.98 and 1000 != 1000.1)

'''3rd program'''
a = (2 * 2 + 2)
b = (2 * (2 + 2))
print(a)
print(b)
print(a == b)

'''4th program'''
srt1 = '123.456'
parts = srt1.split('.')
first_digit_after_dot = parts[1][0]
print(first_digit_after_dot)

'''Первый после точки'''
str2 = '123.456'
float_str2 = float(str2) * 10
print(float_str2)
int_part = int(float_str2)
float_part = int_part % 10
print(int_part)
print(float_part)
