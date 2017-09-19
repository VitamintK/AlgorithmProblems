import random
number = [random.randint(0,1) for x in range(15)]
for i in range(15):
	guess = input()
	if guess == "done":
		print(number)
		break
	print(sum(int(a) != int(b) for a,b in zip(guess, number)))