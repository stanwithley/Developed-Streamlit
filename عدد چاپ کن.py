number = input()
for digit in number:
    print(digit + ":", end=" ")
    if digit != "0":
        print(digit * int(digit))
    else:
        print()
