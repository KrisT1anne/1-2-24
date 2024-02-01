name = []
for i in range(2):
    name.append(input("Hello! What is your name? "))

def reverse_upper(name):
    return name[::-1].capitalize()

result = list(map(reverse_upper, name))

print("Hello, ", result)
