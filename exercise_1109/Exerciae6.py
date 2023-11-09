def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0

sum = addition(10)
print(sum)