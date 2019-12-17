num = input()
n = len(num)

sum = 0

for digit in num:
    sum += int(digit) ** n

if sum == int(num):
    print('narcissist number')
else:
    print('not armstrong')
