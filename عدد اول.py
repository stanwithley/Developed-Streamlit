a = int(input())
b = int(input())
start = min(a, b)
end = max(a, b)
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False 
                break
            i += 1
        if is_prime:
            print(num)
