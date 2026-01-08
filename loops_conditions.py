# Loops and Conditions

text = "learning python for ai"
words = text.split()

count = 0
for word in words:
    count += 1

print("Word count:", count)

num = 12
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
