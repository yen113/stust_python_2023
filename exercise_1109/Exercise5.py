def addition2(a, b):
    def addition1(a, b):
        return a + b
    
    i = addition1(a, b)
    return i + 5

add = addition2(10, 20)
print(add)
