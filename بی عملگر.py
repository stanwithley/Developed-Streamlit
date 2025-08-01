s = input().strip()

# جدا کردن اعداد
parts = s.split('?')
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

# حالت‌ها:
results = []

for op1 in ['+', '*']:
    for op2 in ['+', '*']:
        # حالت پرانتزگذاری: (a op1 b) op2 c
        if op1 == '+':
            first = a + b
        else:
            first = a * b

        if op2 == '+':
            result1 = first + c
        else:
            result1 = first * c

        # حالت پرانتزگذاری: a op1 (b op2 c)
        if op2 == '+':
            second = b + c
        else:
            second = b * c

        if op1 == '+':
            result2 = a + second
        else:
            result2 = a * second

        results.append(result1)
        results.append(result2)

print(max(results))
