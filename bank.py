greeting = input("").lower()
x = greeting[0:5]
if greeting == "hello":
    cash = 0
elif x == "hello":
    cash = 0
elif greeting[0] == "h":
    cash = 20
else:
    cash = 100
print("$", cash)
